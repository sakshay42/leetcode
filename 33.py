class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle

            # know which half is sorted
            if nums[left] <= nums[middle]:  # left is sorted
                if nums[left] <= target < nums[middle]:  # target on left
                    right = middle - 1
                else:
                    left = middle + 1
            else:  # right is sorted
                if nums[middle] < target <= nums[right]:  # target is in right half
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1 
