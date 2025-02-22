class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        degree_count = {}
        for u,v in edges:
            degree_count[u] = degree_count.get(u, 0) + 1
            degree_count[v] = degree_count.get(v, 0) + 1

        for u in degree_count:
            if degree_count[u] == len(degree_count)-1: return u
        """

        # The center must be the common node in the first two edges
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
