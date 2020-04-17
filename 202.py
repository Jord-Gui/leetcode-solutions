# Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        sequence = []
        while n != 1:
            sequence.append(n)
            square_sum = 0
            while n:
                square_sum += (n%10)**2
                n = n//10
            if square_sum in sequence:
                return False
            n = square_sum
        return True
