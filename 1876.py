class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        track = []
        out = 0
        for i in s:
            track = track + [i]
            if len(track) > 3: track = track[1:]
            if len(track) == 3 and len(set(track)) ==3: out= out+1

        return(out) 
