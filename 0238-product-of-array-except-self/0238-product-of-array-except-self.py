class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        left = 1

        for i in range(n):
            answer[i] = left
            left = left * nums[i]

        right = 1

        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right
            right = right * nums[i]

        return answer
        