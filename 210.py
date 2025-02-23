from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for u, v in prerequisites:
            edges[u].append(v)  # Reverse order: v → u


        #give each vertex a state based on where it is on the exploration
        unvisited = 0
        visiting = 1
        visited = 2

        states = [0]*numCourses
        order = []
        #check for cycles and if not found, add them to ordering

        def checkState(vertex):
            if states[vertex] == visiting: return False
            if states[vertex]== visited: return True
            
            states[vertex] = visiting 
            
            for neighbor in edges[vertex]:
                if not checkState(neighbor): 
                    return False

            states[vertex] = visited  # Mark node as visited  
            order.append(vertex)
            return True

        for i in range(numCourses):
            if states[i] == unvisited:
                if not checkState(i): 
                    return []
        
        return order
