class Solution:
    def maxArea(self, height: List[int]) -> int:
        out = 0
        n= len(height)
        left = 0
        right = n-1
        while left < right:
            x = height[left]
            y=height[right]
            area = (right-left)* min(height[right],height[left])
            if x>y: right -= 1
            else: left +=1
            out = max(out,area)
        return(out)
