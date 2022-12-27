"""
Input: s = "abcdefghij", k = 3, fill = "x"
Output: ["abc","def","ghi","jxx"]
"""

def divideString(s, k, fill):
    result = []
    counter = 0
    temp = ""
    for index, item in enumerate(s):
        if counter < 3:
            temp += item
            if index == len(s) - 1 and len(temp) != k:
                target = k - len(temp)
                for i in range(target):
                    temp += fill
                result.append(temp)
            if counter == 2:
                result.append(temp)
                counter = 0
                temp = ""
                continue
            counter += 1
    return result

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        to_ret = []
        while len(s) > 0 :
            to_ret.append(s[:k])
            s = s[k:]
        to_ret[-1] += fill * (k-len(to_ret[-1]))
        return to_ret

if __name__ == "__main__":
    print(divideString("abcdefghij", 3, "x"))