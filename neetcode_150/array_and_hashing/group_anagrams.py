"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""


from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = {}

    for item in strs:
        s = "".join(sorted(item))
        if s in d:
            d[s].append(item)
        else:
            d[s] = [item]

    return list(d.values())


if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams([""]))
    print(groupAnagrams(["a"]))
