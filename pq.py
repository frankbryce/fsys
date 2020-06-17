import re

A = []

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
        A.append(a)
        T.append(a)
    else:
        raise Exception("this is not an axiom")


def _rule1(t):
    h1, h2, h3 = _extractHGroups(t)
    newT = '-'*len(h1) + 'p' + '-'*(len(h2)+1) + 'q' + '-'*(len(h3)+1)
    if newT not in T:
        T.append(newT)

R = [_rule1]
T = A + []
