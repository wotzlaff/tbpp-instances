from itertools import tee

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def get_cliques(s, e):
    n = len(s)
    tss = set(s)
    tes = set(e)
    ts = sorted(tss | tes)
    ndts = [
        t0
        for t0, t1 in pairwise(ts)
        if t0 in tss and t1 in tes
    ]
    return [
        {i for i in range(n) if s[i] <= t and t < e[i]}
        for t in ndts
    ]