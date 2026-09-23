class Solution:
    def find_days(self, weights, capacity):
        total_days = 1
        current_load = 0

        for i in weights:
            if current_load + i > capacity:
                total_days += 1
                current_load = 0
            current_load += i
        return total_days
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            numberofDays = self.find_days(weights, mid)
            if numberofDays <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low 

        