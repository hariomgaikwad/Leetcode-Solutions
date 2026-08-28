class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [0] * n

        i = 0
        j = n - 1

        for k in range(n - 1, -1, -1):
            left = nums[i] * nums[i]
            right = nums[j] * nums[j]

            if left > right:
                temp[k] = left
                i += 1

            else:
                temp[k] = right
                j -= 1
        
        return temp

        