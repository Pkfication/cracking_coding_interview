'''
Using the inbuilt function sorted to 
compare the two strings, without using
any extra space
'''

def isPermutation(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
