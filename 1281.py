# Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sums = 0
        while n > 0:
            current = n%10
            prod *= current
            sums += current
            n = n//10
        return prod - sums
