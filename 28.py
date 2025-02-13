class Solution:

    '''

    ##Issue: goes back and checks everything one by one
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)
        if needle_length > haystack_length: return(-1)
        lower = 0
        upper = 0
        while upper != haystack_length: 
             if needle[lower] == haystack[upper]:
                upper+=1
                lower +=1
             else: 
                upper = upper -lower +1
                lower = 0
             if lower == needle_length:
                return(upper-needle_length)
        return(-1)
     '''
       

    # better if you check the window matches with needle
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)
        if haystack_length < needle_length: return(-1)
        for i in range(0, haystack_length - needle_length + 1):
            if haystack[i:i+needle_length] == needle:
                return(i)
        return(-1)  
         
