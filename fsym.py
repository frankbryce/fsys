def NaiveAddTheorems(R, T, AddTheorem):
    for r in R:
        for t in T.copy():
            AddTheorem(r, t)
