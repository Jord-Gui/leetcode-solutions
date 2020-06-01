# Remove Outermost Parentheses

def removeOuterParentheses(S: str) -> str:
    primitives = []
    parity = 0
    current_primitive = ""
    for bracket in S:
        current_primitive += bracket
        if bracket == "(":
            parity += 1
        else:
            parity -= 1
        if parity == 0:
            primitives.append(current_primitive)
            current_primitive = ""
    for i in range(len(primitives)):
        primitives[i] = primitives[i][1:len(primitives[i])-1]
    ret_val = ""
    for brackets in primitives:
        ret_val += brackets
    return ret_val

print(removeOuterParentheses("(()())(())"))
print(removeOuterParentheses("(()())(())(()(()))"))
