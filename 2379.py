class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = ""
        window_black = 0
        window_white = 0
        out = 0
        for i in blocks:
            if window_black == k: return(0)
            if len(window) == k: 
                if window[0] =='W': window_white -=1
                if window[0] == 'B': window_black -=1
                window= window[1:]
            
            window = window + i
                
            if i == 'W': window_white +=1
            if i == 'B': window_black +=1

            if window_black + window_white ==k: 
                if out==0: out = window_white
                else: out = min(window_white,out)
        return(out)
