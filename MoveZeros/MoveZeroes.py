class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        val = 0
        start = 0
        end = 0
        for start in range(len(nums)):
            if (nums[start] != val):
                nums[end] = nums[start]
                end = end + 1
        numOfZero = len(nums) - end
        for i in range(numOfZero):
            nums[-(i+1)] = 0