"""
Merge 2 sorted lists
Input = [1,3,4,6,8] [2,5,7]
Output = [1,2,4,5,6,7,8]
"""

def merge_arrays(lst1, lst2):
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if(lst1[ind1] > lst2[ind2]):
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1

def merge_lists_2(lst1, lst2):
    # Write your code here
    result = []

    first = 0
    second = 0

    while first < len(lst1) and second < len(lst2):
        if lst1[first] < lst2[second]:
            result.append(lst1[first])
            first += 1
        elif lst1[first] > lst2[second]:
            result.append(lst2[second])
            second += 1

    if first != len(lst1) - 1:
        result.extend(lst1[first:])

    if second != len(lst2) - 1:
        result.extend(lst2[second:])

    return result

if __name__ == "__main__":
    print(merge_lists_2([1,3,4,5], [2,6,7,8]))

#print(merge_arrays([1,3,4,5], [2,6,7,8]))
  