# Number of Different Integers in a String

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        integers = []
        integer = ""
        for char in word:
            if char.isnumeric():
                integer += char
            else:
                if len(integer) > 0 and int(integer) not in integers:
                    integers.append(int(integer))
                integer = ""
        if len(integer) > 0 and int(integer) not in integers:
                integers.append(int(integer))
        return len(integers)