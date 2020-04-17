# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                previous_bracket = stack.pop()
                if previous_bracket in closing_brackets:
                    return False
                elif bracket_pairs[previous_bracket] == bracket:
                    pass
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
