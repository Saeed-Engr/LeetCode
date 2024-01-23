"""class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        ans = [words[0]]
        for i in range(1, len(words)):
            
            dic1 = Counter(ans[-1])
            
            dic2 = Counter(words[i])
            
            if dic1 == dic2:
                continue
            else:
                ans.append(words[i])
                
        return ans"""

class Solution:
    def removeAnagrams(self, words):
        # Initialize the answer list with the first word
        ans = [words[0]]
        
        # Iterate over the words starting from the second one
        for i in range(1, len(words)):
            # Compare the sorted versions of the last word in ans and the current word
            if sorted(ans[-1]) == sorted(words[i]):
                # Skip adding the current word if it is an anagram of the last one in ans
                continue
            else:
                # Add the current word to the answer list if it's not an anagram
                ans.append(words[i])
        
        # Return the final list after removing consecutive anagrams
        return ans


