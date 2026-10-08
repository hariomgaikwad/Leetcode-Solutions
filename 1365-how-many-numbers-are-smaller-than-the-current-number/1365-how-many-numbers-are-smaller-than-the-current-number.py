class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            
            else:
                freq[num] = 1
        
        numbers = sorted(freq.keys())

        smaller_count = {}
        count = 0

        for num in numbers:
            smaller_count[num] = count
            count += freq[num]

        ans = []

        for num in nums:
            ans.append(smaller_count[num])
        return ans  