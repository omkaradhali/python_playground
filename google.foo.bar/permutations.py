def permutation(nums, temp = [], res = []):
    if not len(nums):
        res.append([item for item in temp])
    
    for index, item in enumerate(nums):
        new_nums = [nums[x] for x in range(len(nums)) if x!= index]
        temp.append(item)
        print(new_nums, temp, res)
        permutation(new_nums, temp, res)
        print('here')
        temp.pop()
        print(new_nums, temp, res)
    return res
     
a = permutation([3,1])
# print(a)

x = [''.join(map(str, item)) for item in a]
print(x)