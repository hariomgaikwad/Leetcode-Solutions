class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                ans.append(abs(i))
            else:
                nums[index] = -abs(nums[index])

        return ans       