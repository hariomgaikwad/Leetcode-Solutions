class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        max_sum = float("-inf")

        for i in range(k):
            sum = sum + nums[i]
        max_sum = max(max_sum, sum)

        for i in range(k, len(nums)):
            sum = sum + nums[i]
            sum = sum - nums[i - k]

            max_sum = max(max_sum, sum)

        return max_sum / k


        