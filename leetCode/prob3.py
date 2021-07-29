def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    res = []
    cur = ""
    if len(s) == 1:
        return 1
    for item in s:
        if item not in cur:
            cur = cur + item
        else:
            res.append(cur)
            i = cur.index(item)
            cur = cur[i+1:] + item
    if len(cur):
        res.append(cur)
    res.sort(key=len)
    print(res)
    if len(res):
        return len(res[-1])
    else:
        return 0


print(lengthOfLongestSubstring('dvdf'))
print(lengthOfLongestSubstring('aabccbb'))
