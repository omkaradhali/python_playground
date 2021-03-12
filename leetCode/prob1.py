def dynamic_prob(s):
    
    result = [0 for item in s]
    count = 0
    for index, item in enumerate(s):
        if item == ")":
            # If item is ")" then check immediate left in the string. If "(" then add 2 and attach to result.
            # Checking index - 1 >= 0 to avoid index out of range.
            if index - 1 >= 0 and s[index - 1] == "(":
                # Add the value 2 to whatveer we have one place to the left as we 
                # immediately found the match "(" to the left
                result[index] =  (result[index - 2] if index >= 2 else 0) + 2
                
            
            # This block is in case we find ")" to the left of current position.
            # So we have "))" the last ")" is current index and second last one is ")"
            # We can check if the second last ")" has a matching "(" before to the left.
            # Assuming we have a match "()" before second last ")", we can assume the matching "(" for second
            # last ")"  is one place beyond that hence index - result[index - 1] - 1
            # So assuming we have "(" at index - result[index - 1] -1 we can calculate that the matching "("
            # for last ")" will be one place  beyond that. index - result[index - 1] - 2
            elif index - result[index - 1] - 1 >= 0 and s[index - result[index-1] -1] == "(":
                result[index] = result[index-1] + (result[index - result[index - 1] - 2] if (index - result[index - 1]) >=2 else 0) + 2
            count = max(count, result[index])
            
        else:
            continue
            
    print(count)
    
    # IN case we have to count only sequential brackets like ()
    # seq = 2
    # count = 0
    # retainer = []
    # sol = []
    # for item in s:
    #     if item not in retainer:
    #         seq -= 1
    #         retainer.append(item)
    #         if len(retainer) == 2:
    #             count += 1
    #             sol.append(''.join(retainer))
    #             retainer = []
    #     else:
    #         continue
    
    # print(count)
    # print(sol)
    # return count

dynamic_prob("())((())")
#())((())
# (())(
# )()())