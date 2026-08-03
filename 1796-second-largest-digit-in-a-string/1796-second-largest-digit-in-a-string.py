class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """

        largest = -1
        second_largest = -1

        for ch in s:

            if ch.isdigit():

                digit = int(ch)

                if digit > largest:
                    second_largest = largest
                    largest = digit

                elif digit != largest and digit > second_largest:
                    second_largest = digit

        return second_largest
        

        