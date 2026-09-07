class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()

        count = 0
        j = 0
        n = len(arr2)

        for x in arr1:

            while j < n and arr2[j] < x - d:
                j += 1

            if j == n or arr2[j] > x + d:
                count += 1

        return count
        