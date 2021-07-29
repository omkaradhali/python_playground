"""[summary]
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
"""


def non_repeat_substring(s):
    left = 0
    right = 0
    d = {}
    max_l = 0

    for right in range(len(s)):
        temp = s[right]

        if temp in d:
            left = max(left, d[temp] + 1)

        d[temp] = right
        max_l = max(max_l, (right - left + 1))

    return max_l


if __name__ == "__main__":
    print(non_repeat_substring("aabccbb"))
