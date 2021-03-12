"""
Give 2 strings check if they are anagrams.

'clint eastwood' and 'old west action' are anagrams
'public relations' and 'crap built on lies' are anagrams
'd o g' and 'God' are anagrams.
 Note: ignoring spaces and capitalization.
"""


def anagram_check(s1, s2):
    dict1 = {}
    dict2 = {}
    if len(s1.replace(" ", "")) != len(s2.replace(" ", "")):
        return False

    for item in s1.replace(" ", "").lower():
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] = dict1[item] + 1

    for item in s2.replace(" ", "").lower():
        if item not in dict2:
            dict2[item] = 1
        else:
            dict2[item] = dict2[item] + 1

    if dict1 == dict2:
        return True
    else:
        return False


def anagram_check2(s1, s2):
    str1 = s1.replace(" ", "").lower()
    str2 = s2.replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
        return True

    return False


print(anagram_check2("dog", "GOD"))
