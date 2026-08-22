class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=len(numbers)-1
        right = 0
        while right<left:
            if numbers[right]+numbers[left]>target:
                left-=1
            elif numbers[right]+numbers[left]<target:
                right+=1
            elif numbers[right]+numbers[left]==target:
                return [right+1,left+1]

            
