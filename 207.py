from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        edges = defaultdict(list)
        for u, v in prerequisites:
            edges[u].append(v)
        
        #give each vertex a state based on where it is on the exploration
        unvisited = 0
        visiting = 1
        visited = 2

        states = [0]*numCourses

        def checkStates(vertex):
            if states[vertex] == visiting: return False
            if states[vertex] == visited: return True

            #if vertex is unexplored
            states[vertex] = visiting
            for neighbor in edges[vertex]:
                    if not checkStates(neighbor): return False
            
            states[vertex] = visited
            return True

        for i in range(numCourses):
            if states[i] == unvisited:
                if not checkStates(i):
                    return False
        return True
