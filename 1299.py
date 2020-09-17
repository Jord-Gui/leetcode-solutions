# Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        def getMax(aList):
            current_max = aList[0]
            for num in aList:
                if num > current_max:
                    current_max = num
            return current_max
        
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                current_max = getMax(arr[i+1: len(arr)])
                arr[i] = current_max
        return arr
