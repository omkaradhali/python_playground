"""
Give a sentence reverse it. 
Input: "this is the best"
Output: "best the is this"
"""


def rev_words(s):
    l = s.strip().split(" ")
    print(l)
    result  = []
    
    for item in range(len(l)-1, -1, -1):
        if len(l[item]) == 0: continue
        result.append(l[item])
    
    print(" ".join(result))
            
rev_words("   this is the     best   ")
    
