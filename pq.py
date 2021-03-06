import re

def _extractHGroups(s):
    m = re.match(r'(-+)p(-+)q(-+)', s)
    return m.group(1), m.group(2), m.group(3)

def _isAxiom1(A):
    h1, h2, h3 = _extractHGroups(A)
    if len(h2) != 1:
        return False
    if len(h1) + 1 != len(h3):
        return False
    return True

def AddAxiom(a):
    if _isAxiom1(a):
        A.add(a)
        T.add(a)
    else:
        raise Exception("this is not an axiom")

def AddTheorem(r, t):
    newT = re.sub(r[0], r[1], t)
    T.add(newT)

A = []
T = A | set([])
R = set([
    (r"(-+)p(-+)q(-+)", r"\1p\2-q\3-"),
])

