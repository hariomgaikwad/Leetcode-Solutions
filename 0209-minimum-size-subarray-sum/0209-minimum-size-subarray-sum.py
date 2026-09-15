class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        left = 0
        total = 0
        min_size = float('inf')

        for right in range(len(nums)):

            total += nums[right]

            while total >= target:

                size = right - left + 1
                min_size = min(min_size, size)

                total -= nums[left]
                left += 1

        if min_size == float('inf'):
            return 0

        return min_size
        