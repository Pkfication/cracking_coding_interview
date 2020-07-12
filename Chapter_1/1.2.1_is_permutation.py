'''
Using a map to store the count of characters from the first String and subtracting the count from the map while iterating the second string.

Given the strings are of same length.
'''

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
