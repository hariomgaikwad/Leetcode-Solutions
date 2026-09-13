class Solution:

    def calTotal(self, nums, divisor):
        total = 0

        for num in nums:
            total += math.ceil(num / divisor)

        return total

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        low = 1
        high = max(nums)
        ans = 0

        while low <= high:

            mid = (low + high) // 2

            total = self.calTotal(nums, mid)

            if total <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        