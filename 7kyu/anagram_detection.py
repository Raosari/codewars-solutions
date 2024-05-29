# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

# Examples
# "foefet" is an anagram of "toffee"

# "Buckethead" is an anagram of "DeathCubeK"


# write the function is_anagram
def is_anagram(test, original):
    if len(test) != len(original):
        return False
    test,original = test.lower(),original.lower()
    mapChar = {}
    for ch in test:
        mapChar[ch] = mapChar.get(ch,0) + 1
    
    for c in original:
        mapChar[c] = mapChar.get(c,0) - 1
        if mapChar[c] < 0:
            return False
    return True