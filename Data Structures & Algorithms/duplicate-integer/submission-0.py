class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}

        for i, num in enumerate(nums):
            if num in dict:
                return True
                break
            else:
                dict[num]=i
                 
        return False
            
            
            
        