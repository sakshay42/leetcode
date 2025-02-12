class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_string = str(num)
        l = len(num_string)
        out = 0
        window = num_string[:k]
        if num % int(window) == 0: out +=1
        for i in num_string[k:]:
            window = window[1:] + i
            if int(window)!=0 and num % int(window) == 0:  out +=1
        return(out)
