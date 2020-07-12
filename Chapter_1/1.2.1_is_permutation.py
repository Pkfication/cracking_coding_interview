def isPermutation1(s,t):
    if len(s) != len(t):
        return False
    map = {}
    for i in s:
        if i in map:
            map[i] = map[i] + 1
        else:
            map[i] = 1

    for i in t:
        if i not in map:
            return False
        map[i] = map[i] - 1

    for x in map.values():
        if x != 0:
            return False

    return True
