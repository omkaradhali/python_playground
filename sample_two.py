"""[summary]
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
"""


def longest_substring_with_k_distinct(s, k):
    left = 0
    right = 0
    d = {}
    max_l = 0

    for right in range(len(s)):
        temp = s[right]
        if temp not in d:
            d[temp] = 1
        else:
            d[temp] += 1

        while len(d) > k:
            d[temp] -= 1
            if d[temp] == 0:
                del d[temp]
            left += 1

        max_l = max(max_l, (right - left + 1))

    return max_l


if __name__ == "__main__":
    print(longest_substring_with_k_distinct("araaci", 2))
