class Solution(object):
    def longestPalindrome(self, s):
        window_size = int(len(s)/2)
        starting_pointer = 0
        result = ""

        if len(s) == 2:
            return s[0]

        for i in range(starting_pointer, window_size + 1):
            if s[i] != s[window_size-i]:
                starting_pointer = starting_pointer + 1
                window_size = window_size + 1
            else:
                result += s[i]

        if len(result):
            print(result)
            return result


s = Solution()
print(s.longestPalindrome("abba"))
