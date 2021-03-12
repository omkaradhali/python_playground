def permutation(nums, temp = [], res = []):
    if not len(nums):
        res.append([item for item in temp])
    
    for index, item in enumerate(nums):
        new_nums = [nums[x] for x in range(len(nums)) if x!= index]
        temp.append(item)
        permutation(new_nums, temp, res)
        temp.pop()
    return res
     
a = permutation([3,1,4,1])
print(a)

x = [''.join(map(str, item)) for item in a]
print(x)