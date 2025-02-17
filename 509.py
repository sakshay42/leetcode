class Solution:
    
    """
    def fib(self, n: int) -> int:
        if n==0 or n==1: return(n)
        memo = {0:0,1:1}
        for i in range(2,n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return(memo[n])
    """

#without using dictionary
    def fib(self, n: int) -> int:
        prev = 0
        current = 1
        if n==0 or n==1: return(n)
        for i in range(n-1):
            prev,current = current,current + prev
        return(current)
            
