"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""


def isAnagram(s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}

    for item in s:
        if item in s_dict:
            s_dict[item] += 1
        else:
            s_dict[item] = 1

    for item in t:
        if item in t_dict:
            t_dict[item] += 1
        else:
            t_dict[item] = 1

    return s_dict == t_dict


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat", "car"))
