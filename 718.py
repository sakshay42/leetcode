class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m,n = len(nums1),len(nums2)
        table = [[0]*(n+1) for i in range(m+1)]
        out = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1] == nums2[j-1]: 
                    table[i][j] = 1+table[i-1][j-1]
                    out = max(out,table[i][j])
        return out
        
