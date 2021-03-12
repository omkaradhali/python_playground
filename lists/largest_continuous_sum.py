"""
Given a list of integers (positive and negative)
FInd the largest continuous sum

Input ([1,2,-1,3,4,10,10,-10,-1])
Output 29

"""

def large_cont_sum(arr):
    result  = list()
    largest_sum = 0
    
    for item in arr:
        if len(result) == 0:
            result.append(item)
        else:
            if result[len(result) - 1] + item == 0 :
                result.append(item)
            else:
                result.append(result[len(result) - 1] + item)
    
    max_sum = result[0]
    for item in result:
        if max_sum < item:
            max_sum = item
    
    print(max_sum)
    print(result)

def large_cont_sum2(arr): 
    
    if len(arr)==0:
        return 0
    
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    print(max_sum)
    return max_sum

large_cont_sum([-1,1])
#[-1,1]
#1,2,-1,3,4,10,10,-10,-1