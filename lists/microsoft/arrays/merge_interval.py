"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def merge(intervals):

    if len(intervals) == 1:
        return intervals

    if len(intervals) == 0:
        return []

    left = 0
    right = 1

    intervals.sort()

    while right < len(intervals):
        if intervals[right][0] <= intervals[left][1] <= intervals[right][1]:
            temp = [intervals[left][0], intervals[right][1]]
            intervals = intervals[right + 1:]
            intervals.insert(left, temp)
        elif intervals[right][1] < intervals[left][1]:
            del intervals[right]
        else:
            left += 1
            right += 1

    return intervals


if __name__ == "__main__":
    result = merge([[1, 3], [2, 6], [8, 10], [15, 18]])

    print(result)
    print(merge([[1, 4], [4, 6]]))
    print(merge([[1, 4], [2, 3]]))
