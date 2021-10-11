"""
Generate nth number in fibonacci sequence using
Recursion
Dynamic programming
Iteratively
"""

def iterate_fibo(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
    return a

def recursive_fibo(n):
    if n == 0 or n == 1:
        return n    
    return recursive_fibo(n-1) + recursive_fibo(n-2)

def dynamic_fibo(n):
    cache  = [None] * (n+1)
    
    # Base
    if n == 0  or n == 1:
        return n
    
    # check cache
    if cache[n] != None:
        return cache[n]
    
    # Keeo setting cache
    cache[n] = dynamic_fibo(n-1) + dynamic_fibo(n-2)
    
    
    return cache[n]


if __name__ == "__main__":
    print(iterate_fibo(5))
    print(recursive_fibo(12))
    print(dynamic_fibo(12))