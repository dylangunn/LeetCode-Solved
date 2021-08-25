class Solution:
    def secondHighest(self, s: str) -> int:
        first = -1
        second = -1
        for c in s:
            if c.isnumeric():
                cnum = int(c)
                if cnum == first:
                    continue
                if cnum > first:
                    second = first
                    first = cnum
                elif cnum > second:
                    second = cnum
        return second
                    
        