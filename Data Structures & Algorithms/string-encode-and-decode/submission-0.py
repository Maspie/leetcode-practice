class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            l = str(len(s))
            res += l + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        l = 0
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            
            length = int(s[i:j])
            res.append(s[j+1 : j+1+ length])
            
            i = length + j + 1



        return res
