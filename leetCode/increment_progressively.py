"""
You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.

In one move, you can either:

Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.

Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.


Input: target = 10, maxDoubles = 4
Output: 4
Explanation: Initially, x = 1
Increment once so x = 2
Double once so x = 4
Increment once so x = 5
Double again so x = 10

Input: target = 19, maxDoubles = 2
Output: 7
Explanation: Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19
"""
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0

        while (target > 1):
            if target %2 == 0 and maxDoubles > 0:
                target = target/2
            else:
                target -= 1
            c += 1
        return c

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        to_ret = 0
        while target > 1 :
            if maxDoubles == 0 :
                to_ret += target - 1
                break
            if target % 2 == 1 :
                to_ret += 1
                target -= 1
            else :
                to_ret += 1
                target = target // 2
                maxDoubles -= 1
        return to_ret