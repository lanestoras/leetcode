import string

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for char in s:
            if char in d:
                d[char]+=1
        counts=[]
        for c in d.values():
            if c>0:
                counts.append(c)
        return len(set(counts)) == 1 

            
        