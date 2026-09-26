class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []

        for i in range(0,n):
            ans.append(nums[i])

        for j in range(0,n):
            ans.append(nums[j])
            
        return ans 
        