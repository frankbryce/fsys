import re

def _isAxiom1(A):
    return False

def AddAxiom(a):
    if _isAxiom1(a):
        A.append(a)
        T.append(a)
    else:
        raise Exception("this is not an axiom")

def AddTheorem(r, t):
    newT = re.sub(r[0], r[1], t)
    if newT not in T:
        T.append(newT)

A = []
T = A + []
R = [
    (r"", r""),
]

