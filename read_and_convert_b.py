import os
import zipfile

from utils import get_cliques

taus = [5, 15] + list(range(10, 200+1, 10)) + list(range(250, 750+1, 50))
for tau in taus:
    sub = '1' if tau <= 200 else '2'
    os.makedirs(f'data/b{sub}/{tau}', exist_ok=True)

with zipfile.ZipFile('./raw/tkp.zip') as zf:
    for idx in range(1, 100 + 1):
        with zf.open(f'all/I{idx}') as fh:
            lines = fh.readlines()
            n = int(lines[0])
            cap = int(lines[1])
            items = [
                [int(v) for v in line.split()[1:] if v]
                for line in lines[2:][:n]
            ]
            c = [item[0] for item in items]
            s = [item[1] for item in items]
            e = [item[2] for item in items]
            cs = get_cliques(s, e)
            for tau in taus:
                items = sorted({
                    i
                    for csk in cs[:tau]
                    for i in csk
                })
                n = len(items)
                sub = '1' if tau <= 200 else '2'
                with open(f'data/b{sub}/{tau}/I_{idx}.txt', 'w') as fh:
                    fh.write(f'{n}\t{cap}\t0\t0\n')
                    for i in range(n):
                        fh.write(f'{i}\t{s[i]}\t{e[i]}\t{c[i]}\n')
