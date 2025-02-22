from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        #Convert edge set into a dictionary

        edge_dict = {}
        for u,v in edges:
            edge_dict.setdefault(u,[]).append(v)
            edge_dict.setdefault(v,[]).append(u)
        
        seen = set()
        seen.add(source)
        
        
        """

        #DFS with recursion
        def dfs(v):
            if v==destination: return True #if you have hit that vertex return true, don't search it's neighbors
            
            for neighbor in edge_dict[v]: #you have not found the vertex, look at the neighbors of vertex v and see if you can find a path from the neighbors to destination
                if neighbor not in seen:
                    seen.add(neighbor) #already seen the neighbor, don't search again
                    if dfs(neighbor): return True #there is a path 
            
            return False #didn't find it then there's no path

        
        return dfs(source)
        """   





        """
        #dfs with stack
        stack = [source]
        while stack:
            node = stack.pop() #remove the most recent node
            if node== destination:
                return True
            else:
                for neighbor in edge_dict[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)

        return False
        """
        q = deque()
        q.append(source)

        while q:
            node = q.popleft()
            if node==destination: return True

            for neighbor in edge_dict[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)
        return False













