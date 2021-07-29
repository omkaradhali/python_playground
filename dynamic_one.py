"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


def uniquePaths(m, n):
    if m == 1 or n == 1:
        return 1

    return uniquePaths(m, n-1) + uniquePaths(m-1, n)


print(uniquePaths(3, 2))
