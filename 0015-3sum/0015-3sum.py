class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
            
        ans = []
        n = len(nums)
        nums.sort()   # sort first for two-pointer technique

        for i in range(0,n):
                # skip duplicate fixed elements
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # set up the two pointer
            j = i + 1
            k = n - 1

            # Move pointer toward each other
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:  # need a larger sum
                    j += 1
                elif total_sum > 0:  # need a smaller sum

                    k -= 1
                else:
                    # Found a valid triplet
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)

                    # Move both pointer ans skip duplicates
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans        