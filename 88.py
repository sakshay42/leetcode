class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        top = m-1
        bottom =n-1
        merge_index = m + n - 1  
        
        while bottom >= 0:
            if nums1[top] > nums2[bottom] and top >=0:
                nums1[merge_index] = nums1[top] 
                top -=1
            else: 
                nums1[merge_index] = nums2[bottom]
                bottom -=1
            merge_index -= 1

        
            
        
        
