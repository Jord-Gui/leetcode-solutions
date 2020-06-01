# Remove Outermost Parentheses

def removeOuterParentheses(S: str) -> str:
    primitives = []
    stack = []
    current_primitive = ""
    for bracket in S:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            current_primitive = stack.pop() + current_primitive + bracket
        if len(stack) == 0:
            primitives.append(current_primitive)
            current_primitive = ""
    return primitives

print(removeOuterParentheses("(()())(())"))
