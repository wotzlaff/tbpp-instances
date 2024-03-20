import os
import numpy as np
import pandas as pd


def main():
    data = pd.read_parquet('azure.parquet.gzip')
    data['d'] = data['e'] - data['s']

    def write_file(df, cap, filename):
        n = df.shape[0]
        with open(filename, 'w') as fh:
            fh.write(f'{n}\t{cap}\t0\t0\n')
            for i in range(n):
                fh.write(
                    '\t'.join([str(i)] + [f'{df[k][i]}' for k in ['s', 'e', 'c']])
                    + '\n'
                )

    ns = [
        n
        for c1 in [10**k for k in [2, 3, 4]]
        for c0 in [1, 2, 5]
        if (n := c0 * c1) <= 10000
    ][::-1]

    rng = np.random.default_rng(42)
    os.makedirs('data/d1', exist_ok=True)
    os.makedirs('data/d2', exist_ok=True)

    data_subs = [
        (tau, data[(data['d'] >= 24 / tau * 60) & (data['d'] < 24 * 60)])
        for tau in [2, 4, 8, 24]
    ] + [('inf', data[data['d'] < 24 * 60])]
    for tau, data_sub in data_subs:
        for sample in range(10):
            idx = rng.permutation(data_sub.index)
            for n in ns:
                idx0 = sorted(idx[:n])
                c = '1' if n <= 1000 else '2'
                filename = f'data/d{c}/{n}_{tau}_{sample+1}.txt'
                write_file(
                    data_sub.loc[idx0].reset_index(drop=True),
                    100,
                    filename,
                )


if __name__ == '__main__':
    main()
