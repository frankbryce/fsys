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

def AddTheorem(r, *ts):
    for t in ts:
        assert t in T
    assert r in R
    r = r.split(">>")
    rs = r[0].split(',')
    if len(rs) != len(ts):
        return
    newT = r[-1]
    for i, rl in enumerate(rs):
        ms = re.match(r'^{}$'.format(rl), ts[i])
        if not ms:
            return
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
    # required for multi-theorem rules
    assert ',' not in t


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

