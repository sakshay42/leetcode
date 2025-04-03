class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = set()
        for i in range(n-2):
            left = i+1
            right = n-1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] > target:
                    right -=1
                elif nums[left] + nums[right] < target:
                    left +=1
                else:
                    triplets.add((nums[i],nums[left],nums[right]))
                    while left < right and nums[left] == nums[left+ 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return list(map(list,triplets))
