def permute(s):
    
    out = []
    print("Begin permute block : {}, out {}".format(s, out))
    # Base Case
    if len(s) == 1:
        out = [s]
        
    else:
        # For every letter in string
        for i, let in enumerate(s):
            print("Looping {} first character {}".format(s,let))
            print("iterating through {}".format(s[:i] + s[i+1:]))
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):
                
                print(out,let,perm)
                # Add it to output
                out += [let + perm]

    return out

def permute_num(n):
    
    out = []
    if len(str(n)) == 0 or len(str(n)) == 1:
        return n
    
    for i, let in enumerate(str(n)):
        
        for perm in permute_num(str(n[:i]) + str(n[i+1:])):
            out += [str(let) + str(perm)]
    
    return [int(x) for x in out]


if __name__ == "__main__":
    print(permute('abc'))
    print(permute_num('123'))