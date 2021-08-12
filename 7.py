# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        reverse_x = ""
        if x > 0:
            for num in range(len(str_x)):
                reverse_x = str_x[num] + reverse_x
        elif x == 0:
            reverse_x = 0
        else:
            for num in range(1, len(str_x)):
                reverse_x = str_x[num] + reverse_x
            reverse_x = "-" + reverse_x
        reverse_x = int(reverse_x)
        if reverse_x > (2**31 - 1) or reverse_x < (-2**31):
            return 0
        else:
            return reverse_x
