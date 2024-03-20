import os
import sys
import sqlalchemy
import pandas as pd


def main():
    assert len(sys.argv) == 2, 'no file specified'
    db = sys.argv[1]
    assert os.path.exists(db), 'file not found'
    engine = sqlalchemy.create_engine('sqlite:///' + db)

    with engine.connect() as conn, conn.begin():
        vms = pd.read_sql_query(
            """
            SELECT * FROM `vm`
            LEFT JOIN (
                SELECT `vmTypeId`, MAX(`core`) as `maxCore`
                FROM `vmType` GROUP BY `vmTypeId`
            ) AS `vmType` ON `vm`.`vmTypeId` = `vmType`.`vmTypeId`
            WHERE `maxCore` < 1 - 0.25
            AND `maxCore` >= 0.25
            AND (`starttime` >= 0 OR `endtime` IS NOT NULL)
        """,
            conn,
        )

    vms['s'] = (vms['starttime'].clip(lower=0.0) * 24 * 60).round().astype(int)
    vms['e'] = (
        (vms['endtime'].fillna(14.0).clip(upper=14.0) * 24 * 60).round().astype(int)
    )
    vms.loc[vms['e'] == vms['s'], 'e'] += 1
    vms['c'] = (vms['maxCore'] * 100).astype(int)
    vms = vms[['s', 'e', 'c']]
    vms = vms.sort_values(by=['s', 'e']).reset_index(drop=True)
    vms.to_parquet('azure.parquet.gzip', compression='gzip')


if __name__ == '__main__':
    main()
