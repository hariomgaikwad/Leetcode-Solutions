# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        freq = {}
        temp = head

        dummy = ListNode(0)
        tail = dummy

        while temp is not None:
            if temp.val not in freq:
                freq[temp.val] = True

                tail.next = ListNode(temp.val)
                tail = tail.next

            temp = temp.next

        return dummy.next