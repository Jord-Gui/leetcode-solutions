# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x > 2**31 - 1 or x < -2**31:
            return 0
        elif x < 0:
            x = x*-1
            ret_val = "-"
        else:
            ret_val = ""
        while x != 0:
            ret_val += str(x % 10)
            if int(ret_val) > 2**31 - 1 or int(ret_val) < -2**31:
                return 0
            x = x // 10
        return int(ret_val)
