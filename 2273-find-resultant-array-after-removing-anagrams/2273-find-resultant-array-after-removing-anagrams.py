class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        ans = [words[0]]
        for i in range(1, len(words)):
            
            dic1 = Counter(ans[-1])
            
            dic2 = Counter(words[i])
            
            if dic1 == dic2:
                continue
            else:
                ans.append(words[i])
        return ans
            