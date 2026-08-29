class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for i in strs:
            Count = [0] * 26

            for n in i:
                
                Count[ord(n) - ord('a')] += 1

            
            res[tuple(Count)].append(i)

        return list(res.values())

