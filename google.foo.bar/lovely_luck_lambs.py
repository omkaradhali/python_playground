def solution(total_lambs):
    # Your code here
    square_list = find_square_list(total_lambs)
    fib_list = find_fib_sequence(total_lambs)
    print(square_list)
    print(fib_list)
    
    print("LENGTH")
    print(len(square_list), sum(square_list))
    print(len(fib_list), sum(fib_list))
    return abs(len(fib_list) - len(square_list))

def find_square_list(n):
    res = []
    
    if n > 0:
        res.append(1)
    else:
        return []
    
    x = 1
    next_val = 2**x
    
    while next_val <= n:
        res.append(next_val)
        x = x + 1
        next_val = 2**x
        if sum(res) + next_val > n:
            a = res[-1] + (next_val - res[-1])/2
            if  sum(res) + a < n:
                next_val = a
            z = [0.1, 0.2, 0.25, 0.5]
            for i in z:
                a = res[-1] +(next_val - res[-1])/2
                if sum(res) + a > n:
                    continue
                else:
                    next_val = a
                    break
            # next_val = sum(res) + next_val**(0.5)
        if sum(res) > n or sum(res) + next_val > n:
            break
    
    return res

def find_fib_sequence(n):
    
    res = []
    next_val = 0
    if n >= 0:
        res.append(1)
    if n > 1:
        res.append(1)
    
    
    if len(res) >=2 and res[-1] and res[-2]:
        next_val = res[-1] + res[-2]
    
    y = 3
    while next_val <= n:
        res.append(next_val)
        next_val = res[y-1] + res[y-2]
        if sum(res) > n or sum(res) + next_val > n:
            break
        y = y + 1
        
    return res

print(solution(143))
#917503