"""
Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat.
"""

def brute_force(start, end, dt):
    if len(start) != len(end):
        return null
    
    if not dt:
        return null
    
    result_set = []
    result_set.append(start)
    
    for i in reversed(range(len(start))):
        result_string = ""
        
        if i == 0:
            result_string = end[i:len(end)]
            result_set.append(result_string)
            
        if i != 0:
            result_string = start[0:i] + end[i:len(end)]
            result_set.append(result_string)
        
    print(result_set)
    for item in result_set:
        if item == start:
            continue

        if item in dt:
            continue
        else:
            print("item {} not found".format(item))
            return None
    
    return result_set

# Solution from dailycoding.
from collections import deque
import string

def word_ladder(start, end, words):
    queue = deque([(start, [start])])

    while queue:
        word, path = queue.popleft()
        if word == end:
            return path

        for i in range(len(word)):
            for c in ascii_lowercase:
                next_word = word[:i] + c + word[i + 1:]
                if next_word in words:
                    words.remove(next_word)
                    queue.append([next_word, path + [next_word]])

    return None        
        

#print(brute_force("dog", "cat", {"dot", "tod", "dat", "dar"})) #{"dot", "tod", "dat", "dar"}

print(word_ladder("dog", "cat", {"dot", "tod", "dat", "dar"}))
# ["dog", "dot", "dat", "cat"] 
        
    
    
    
    