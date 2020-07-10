def one_away(str1, str2):
    if str1 == str2: return True
    if abs(len(str1) - len(str2)) > 1: return False

    s1 = str1 if len(str1) > len(str2) else str2
    s2 = str2 if len(str1) > len(str2) else str1

    index1,index2,diff = 0,0, False
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if diff: return False
            diff = True
            if index1 != index2:
                return False
        else:
            index2 += 1
        index1 += 1
    return True
