'''
We keep two variables pointing to the current letter
and current count. Update the letter and count as we
iterate through the string.
'''

def str_compression(s1):
    if len(s1) < 3: return s1

    s = ""
    letter = s1[0]
    count = 1
    for i in range(1, len(s1)):
        if s1[i] == letter:
            count += 1
        else:
            s += letter + str(count)
            letter = s1[i]
            count = 1
    s += letter + str(count)
    return s1 if len(s) > len(s1) else s
