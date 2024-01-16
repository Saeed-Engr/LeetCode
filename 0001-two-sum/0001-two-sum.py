class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {} # create empty dictionary
        
        for i, num in enumerate(nums):   # i=0,its a index and num is value of 0 index
                                        # Example, nums = [2,7,11,15], target = 9
                                        # i = 0, num=2 so on
            complement = target - num
            
            if complement in num_dic:
                return [num_dic [complement], i]
            
            num_dic[num] = i
            
                