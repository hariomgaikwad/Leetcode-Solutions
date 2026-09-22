class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n = len(arr)
        if n < k:
            return 0

        total = 0
        count = 0

        for i in range(0, k):
            total = total + arr[i]

        if total / k >= threshold:
            count += 1

        for j in range(k, n):
            total = total + arr[j]
            total = total - arr[j - k]

            if total / k >= threshold:
                count+= 1
        
        return count 

        