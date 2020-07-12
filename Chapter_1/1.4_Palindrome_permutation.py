'''
Palindrome is a string or a phrase which is same backwards and forwards. Permutation is same characters with different order. 

The above definition gives us the clue that, we need to have the characters in even count, except for one odd count. if the odd count is more than 1, we can assume that it is not a PalindromePermutation.
'''

NO_OF_CHARS = 256

def isPalindromePermuation(st):

    count = [0] * (NO_OF_CHARS)
    for i in range( 0, len(st)) :
        count[ord(st[i])] = count[ord(st[i])] + 1

    odd = 0

    for i in range(0, NO_OF_CHARS ) :
        if (count[i] & 1) :
            odd = odd + 1
        if (odd > 1) :
            return False

    return True
