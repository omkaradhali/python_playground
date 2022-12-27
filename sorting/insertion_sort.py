def insertion_sor(lst: list) -> list:
  for i, num in enumerate(lst):
    current  = i
    while current > 0 and lst[current] < lst[current - 1]:
      lst[current], lst[current - 1] = lst[current - 1], lst[current]
      current -= 1
  return lst

if __name__ == "__main__":
  lst  = [1,3,2,4,9,0]
  sorted_list = insertion_sort_with_for_loop(lst)
  print(sorted_list)