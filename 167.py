class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        left = 0
        right = n-1
        while left < right:
            x =numbers[left]
            y = numbers[right ]
            if  x+y  == target: return [left+1,right+1]
            elif x + y > target: right = right -1
            else: left = left + 1

## Just store sum 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left= 0
        right = n-1
        while right > left:
            total = numbers[left] + numbers[right]
            if  total == target:
                return [left+1,right+1]
            elif total > target: right -=1
            else: left +=1
        
        
