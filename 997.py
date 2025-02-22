class Solution:
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        edge_dict = {}
        if n==1: return 1
        for u,v in trust:
            edge_dict.setdefault(v,[0,0])[1] +=1
            edge_dict.setdefault(u,[0,0])[0] +=1

        for i in edge_dict:
            if edge_dict[i] == [0,n-1]: return i
        
        return -1 
    """

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0]*n
        for u,v in trust:
            count[u-1] -=1 # penalise if you trust anyone
            count[v-1] +=1  # credit if anyone trusts you
        
        for i in range(n):
            if count[i] == n-1:
                return i+1
        
        return -1
