import re

def _isAxiom1(a):
    return a in A

def AddAxiom(a):
    if _isAxiom1(a):
        A.add(a)
        T.add(a)
    else:
        raise Exception("this is not an axiom")

def AddTheorem(r, t):
    assert t in T
    assert r in R
    newT = re.sub(r'^{}$'.format(r[0]), r[1], t)
    T.add(newT)

A = set(['N-'])
T = A | set([
])
R = set([
    (r"N(-+)", r"N\1-"),
    (r"N(-+)", r"\1A\1A\1"),
    (r"(-+)A(-+)A-(-+)", r"\1\2A\2A\3"),
    (r"(-+)A-+A-", r"S\1"),
])

