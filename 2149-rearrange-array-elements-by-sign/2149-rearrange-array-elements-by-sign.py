class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = n * [0]
        pos_index = 0
        neg_index = 1
        for i in range(0, n):
            if nums[i] >= 0:
                result[pos_index] = nums[i]
                pos_index += 2
            else:
                result[neg_index] = nums[i]
                neg_index += 2
                
        return result
        