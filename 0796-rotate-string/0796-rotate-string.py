class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        double_s = s + s
        if goal in double_s :
            return True
        return False
        