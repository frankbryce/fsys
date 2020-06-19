import re

def _isAxiom1(a):
    return a in A

def AddAxiom(a):
    if _isAxiom1(a):
        VerifyTheorem(a)
        A.add(a)
        T.add(a)
    else:
        raise Exception("this is not an axiom")

def AddTheorem(r, t):
    assert t in T
    assert r in R
    r = r.split(">>")
    ms = re.match(r[0], t)
    if not ms:
        return
    newT = r[-1]
    for name, m in ms.groupdict().items():
        newT = re.sub(r'\?<{}>'.format(name), m, newT)
    VerifyTheorem(newT)
    T.add(newT)

# verify that no illegal characters are in theorems
def VerifyTheorem(t):
    # required for encoding named capture groups.
    assert '(' not in t
    assert 'P' not in t
    assert '?' not in t
    assert '<' not in t
    assert '>' not in t
    assert ')' not in t
    # required for encoding non-capturing group
    assert ':' not in t
    # required forformula


A = set(['N-'])
T = A | set([
])
for t in T:
    VerifyTheorem(T)
R = set([
    r"N(?P<x>-+)>>N?<x>-",
    r"N(?P<x>-+)>>?<x>A?<x>A?<x>",
    r"(?P<x>-+)A(?P<y>-+)A-(?P<z>-+)>>?<x>?<y>A?<y>A?<z>",
    r"(?P<x>-+)A-+A->>S?<x>",
])

