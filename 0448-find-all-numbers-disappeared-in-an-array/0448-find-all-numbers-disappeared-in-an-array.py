class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in nums:
            index = abs(i) - 1
            nums[index] = -abs(nums[index])

        ans = []
        for i in range(0,n):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans 

        