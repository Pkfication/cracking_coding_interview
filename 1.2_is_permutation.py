def isPermutation(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
