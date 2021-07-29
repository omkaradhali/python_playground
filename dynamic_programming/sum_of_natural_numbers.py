"""
Given a number find the sum of all numbers upto that number
"""


def sum_of_all_natural_numbers(num):
    if num <= 1:
        return num
    
    return num + sum_of_all_natural_numbers(num - 1)


if __name__ == "__main__":
    print(sum_of_all_natural_numbers(100))