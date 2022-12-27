from typing import List

def selection_sort(lst: List[int])  -> List[int]:
  # 1. Loop through all the elements considering the first element as minimum.
  # 2. Start another loop after first element 
  for i in range(0, len(lst) - 1):
    min_value = i
    
    for j in range(i, len(lst)):
      if lst[j] < lst[min_value]:
        min_value = j

    if min_value != i:
      lst[min_value], lst[i] = lst[i], lst[min_value]
  
  return lst



if __name__ == "__main__":
  lst  = [1,5,3,2,9]
  sorted_list = selection_sort(lst)
  print(sorted_list)