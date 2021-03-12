from stack import Stack
def check_balance(s):
    
    stack = Stack()
    
    for item in s:
        s_i = ""
        if stack.size():
            s_i = stack.peek()
        
        if item == "{" or item =="(" or item == "[":
            stack.push(item)
            continue
        
        if item == ")" and s_i == "(":
            stack.pop()  
        elif item == "}" and s_i == "{":
            stack.pop()
        elif item == "]" and s_i == "[":
            stack.pop()
        else:
            stack.push(item)
        
    if stack.size():
        return False
    else:
        return True

print(check_balance("(({())){{{}}}"))