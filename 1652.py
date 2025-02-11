1652class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
       l = len(code)
       decode = [0]*l
       if k==0: return(decode)
       elif k>0: 
         decode[0] = window_sum = sum(code[1:k+1])
         for i in range(1,l):
            window_sum = window_sum + code[(i+k)% l] - code[i%l]
            decode[i] = window_sum 
       else:
        window_sum = sum(code[k:])  
        decode[0] = window_sum
        for i in range(1,l):  
                window_sum = window_sum + code[(i-1)%l] - code[(i+k-1) % l]
                decode[i] = window_sum
        
       return(decode)
