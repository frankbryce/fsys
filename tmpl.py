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
    assert r in R
    assert t in T
    newT = re.sub(r[0], r[1], t)
    T.add(newT)

A = set([])
T = A | set([])
R = set([
    (r"", r""),
])

