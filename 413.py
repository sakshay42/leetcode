class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        out = 0
        current =0 
        for i in range(2,len(nums)):
            if nums[i] + nums[i-2] == 2*nums[i-1]:
                current +=1 #keep checking in window of size 3 if it an AP
                out += current # if there are k consecutive windows of size k then 1+2+..+k ap subarrays of size >=3 
            else: current = 0 #not an ap then move the window
        return(out)



#same but left and right pointers
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        left =0 
        out = 0
        for right in range(1,len(nums)-1):
            if nums[right-1] + nums[right+1] == 2*nums[right]:
                out += right-left
            else: 
                left = right
        
        return out
