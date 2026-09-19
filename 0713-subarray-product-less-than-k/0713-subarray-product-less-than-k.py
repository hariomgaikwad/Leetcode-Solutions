class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0
        n = len(nums)
        for right in range(0, n):
            product *= nums[right]

            while product >= k:
                product = product // nums[left]
                left += 1

            count += right - left + 1
        
        return count 
        