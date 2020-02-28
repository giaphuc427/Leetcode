from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for row,i in enumerate(nums):
            for j in range(nums.index(i)+1,len(nums)):
                if target == i + nums[j]:
                    return [row, j]
            
nums = [2,7,11,15]
target = 18
ins = Solution()
print(ins.twoSum(nums, target))