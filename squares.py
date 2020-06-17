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
    newT = re.sub(r'^{}$'.format(r[0]), r[1], t)
    if newT not in T:
        T.append(newT)

A = ['N-']
T = A + []
R = [
    (r"N(-+)", r"N\1-"),
    (r"N(-+)", r"\1A\1A\1"),
    (r"(-+)A(-+)A-(-+)", r"\1\2A\2A\3"),
    (r"(-+)A-+A-", r"S\1"),
]

