def NaiveAddTheorems(R, T, AddTheorem):
    for r in range(len(R)):
        for t in range(len(T)):
            AddTheorem(R[r], T[t])
