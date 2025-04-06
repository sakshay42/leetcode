class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        left_wall = 0
        right_wall = 0
        max_left = [0]*n 
        max_right = [0]*n
        for i in range(len(height)):
            j = -i-1
            max_left[i] = left_wall
            max_right[j] = right_wall
            left_wall = max(left_wall,height[i])
            right_wall = max(right_wall,height[j])
        water = 0
        for i in range(len(height)):
            water += max(0, min(max_left[i],max_right[i])- height[i])
        return water
