"""
Remove all the even elements from given array

Input  : [1,2,4,5,3,6,7]
Output : [1,5,3,7]
"""

def remove_even(ar):
    res  = []
    for item in ar:
        if item % 2 != 0:
            res.append(item)
            
    print(res)
    return res

def remove_even_list_comprehension(list):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in list if number % 2 != 0]

remove_even([1,2,4,5,3,6,7])