# Remove Outermost Parentheses

def removeOuterParentheses(S: str) -> str:
    primitives = ""
    parity = 0
    current_primitive = ""
    for bracket in S:
        current_primitive += bracket
        if bracket == "(":
            parity += 1
        else:
            parity -= 1
        if parity == 0:
            primitives += current_primitive[1:len(current_primitive)-1]
            current_primitive = ""
    return primitives

print(removeOuterParentheses("(()())(())"))
print(removeOuterParentheses("(()())(())(()(()))"))
