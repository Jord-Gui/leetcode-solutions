# Split a STring in Balanced Strings

class Solution:  
    def balancedStringSplit(self, s: str) -> int:
        output = 0
        parity = 0
        for char in s:
            if char == "R":
                parity += 1
            else:
                parity -= 1
            if parity == 0:
                output += 1
        return output
