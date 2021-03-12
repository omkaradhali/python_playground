def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    ind1 = 0 
    ind2 = 0
    while ind1 < len(nums1) and ind2 < len(nums2):
        if(nums1[ind1] > nums2[ind2]):
            # insert list2's current index to list1
            nums1.insert(ind1, nums2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(nums2):  # Append whatever is left of list2 to list1
        nums1.extend(nums2[ind2:])

    
    if len(nums1) % 2 == 0:
        print(nums1[len(nums1)/2], nums1[(len(nums1)/2) - 1])
        return (nums1[len(nums1)/2] + nums1[(len(nums1)/2) - 1]) / 2.0
    else:
        return nums1[len(nums1)/2]

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         l = nums1 + nums2
#         l.sort()
#         if len(l) == 1:
#             return l[0]
#         if len(l)%2 == 0:
#             return float(l[len(l)//2-1] + l[len(l)//2])/2
#         return l[len(l)//2]
print(findMedianSortedArrays([1,2],[3,4]))