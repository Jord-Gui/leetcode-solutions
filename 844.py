# Backspace String Compare

def backspace(S):
    S = list(S)
    i = 0
    while i < len(S):
        if S[i] == "#":
            if i-1 >= 0:
                S.pop(i)
                S.pop(i-1)
                i -= 1
            else:
                S.pop(i)
        else:
            i += 1
    return "".join(S)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = backspace(S)
        T = backspace(T)
        if S == T:
            return True
        return False


# can use a stack instead to optimise O(n)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS = []
        stackT = []
        for i in S:
            if i != "#":
                stackS.append(i)
            else:
                if stackS:
                    stackS.pop()
        
        for i in T:
            if i != "#":
                stackT.append(i)
            else:
                if stackT:
                    stackT.pop()
        return stackS==stackT