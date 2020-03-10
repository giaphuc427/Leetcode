class Solution:
    def searchInsert(self, nums, target):
        pivot = int(len(nums)/2)
        for i in range(int(len(nums) / 2)):
            if (pivot == 0 & nums[pivot] != target):
                return -1
            if (nums[pivot] == target):
                return nums.index(target)
            elif (nums[pivot] > target):
                searchInsert(nums[:pivot],target)
            else:
                searchInsert(nums[pivot:],target)

nums = [1,2,3,4,5,6]
target = 3
a = Solution()
print(a.searchInsert(nums,target))