# Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        elif n == 3:
            return [-1, 0, 1]
        elif n%2 == 1:
            arr = [-1, 0, 1]
            n -= 3
            num = 2
            while n > 0:
                arr.append(num)
                arr.append(-num)
                num += 1
                n -= 2
            return arr
        else:
            arr = []
            for i in range(1, (n//2)+1):
                arr.append(i)
                arr.append(-i)      
            return arr
