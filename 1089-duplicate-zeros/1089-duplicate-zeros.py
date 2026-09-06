class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)

        zeros = 0

        # Count zeros that can be duplicated
        for i in range(n):
            if arr[i] == 0:
                zeros += 1

        # Start from the last element
        i = n - 1
        j = n + zeros - 1

        while i >= 0:
            if j < n:
                arr[j] = arr[i]

            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0

            i -= 1
            j -= 1
        """
        Do not return anything, modify arr in-place instead.
        """

        