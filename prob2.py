"""
Given an array of integers, return a new array such that each element at index i of the new array is the 
product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# Brute method O(n)
def brute_force(lst):
    
    total_prod = 1
    result = []
    
    for item in lst:
        total_prod = total_prod * item
        
    for item in lst:
        result.append(total_prod/item)
    
    print(result)
    
# Brute method without division O(n^2)
def brute_two(lst):
    
    result  = []
    prod = 1
    
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                prod = prod*lst[j]
        result.append(prod)
        prod = 1 
    
    print(result)

# O(n) Without division
def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        print("num : {}".format(num))
        print("before confitons --> {}".format(suffix_products))
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
        print("after confitons --> {}".format(suffix_products))
    suffix_products = list(reversed(suffix_products))
    print(suffix_products)
    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result 

# brute_force([1,2,3,4,5])
# brute_two([3,2,1])
print(products([1,2,3,4,5]))