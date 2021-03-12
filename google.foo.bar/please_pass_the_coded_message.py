"""
You need to pass a message to the bunny prisoners, but to avoid detection, 
the code you agreed to use is... obscure, to say the least. The bunnies are 
given food on standard-issue prison plates that are stamped with the 
numbers 0-9 for easier sorting, and you need to combine sets of plates to 
create the numbers in the code. The signal that a number is part of the 
code is that it is divisible by 3. You can do smaller numbers like 15 and 
45 easily, but bigger numbers like 144 and 414 are a little trickier. Write 
a program to help yourself quickly create large numbers for use in the 
code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function 
solution(L) which finds the largest number that can be made from some or 
all of these digits and is divisible by 3. If it is not possible to make 
such a number, return 0 as the solution. L will contain anywhere from 1 to 
9 digits.  The same digit may appear multiple times in the list, but each 
element in the list may only be used once.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases -- 
Input:
Solution.solution({3, 1, 4, 1})
Output:
    4311
    
Input:
Solution.solution({3, 1, 4, 1, 5, 9})
Output:
    94311

-- Python cases -- 
Input:
solution.solution([3, 1, 4, 1])
Output:
    4311

Input:
solution.solution([3, 1, 4, 1, 5, 9])
Output:
    94311
"""
def solution(l):
    # Your code here
    result_list = permutation(l)
    # print(result_list)
    result_list.sort()
    
    if len(result_list):
        return result_list[-1]
    else:
        return 0
    


def permutation(nums, temp = [], result = [], fin_res = []):
    if not len(nums):
        # print(temp)
        c = check_if_divisible_by_3(temp)
        if c != 0:
            fin_res.append(c)
        result.append([item for item in temp])
    
    for index, item in enumerate(nums):
        new_nums = [nums[x] for x in range(len(nums)) if x!= index]
        temp.append(item)
        
        temp_num = check_if_divisible_by_3(temp)
        new_num_num = check_if_divisible_by_3(new_nums)
        
        if temp_num != 0:
            fin_res.append(temp_num)
        
        if new_num_num != 0:
            fin_res.append(new_num_num)
            
        permutation(new_nums, temp, result)
        temp.pop()
    return fin_res

def check_if_divisible_by_3(ar):
    # print(ar)
    if len(ar):
        s = ''.join(map(str,ar))
        x = int(s)
        # print(x)
        if x % 3 == 0:
            return x
        
        return 0
    
    return 0


	
from itertools import combinations
 
def answer(l):
	l = l.sort(reverse = True)
	for i in reversed(range(1, len(l) + 1)):
		for tup in combinations(l, i):
			if sum(tup) % 3 == 0: return int(''.join(map(str, tup)))
	return 0

print(answer([3, 1, 4, 1]))