class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:return False
        window = [nums[0]]    #keep a list elements in the window
        window_length = 1
        out = False
        for i in range(1,len(nums)): #keep moving to the right
            if nums[i] in window: 
                 return(True) #if this element is in the window, you've found it
            else: 
                 if window_length ==k: #once you reach a window sizd k then just add to thr right and remove the left
                    window = window[1:] 
                    window.append(nums[i])
                 else: 
                    window.append(nums[i])
                    window_length =  window_length+1
        return(out)




