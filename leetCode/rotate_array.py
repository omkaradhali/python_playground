def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    arr_length = len(nums)
    tail_count = arr_length - k

    result = [0 for i in nums]

    while tail_count < len(nums):
        result[(tail_count - 1 - k)] = nums[tail_count]
        tail_count += 1

    for i in range(3, len(nums)):
        result[i] = nums[i - k]

    return result


if __name__ == "__main__":
    print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
