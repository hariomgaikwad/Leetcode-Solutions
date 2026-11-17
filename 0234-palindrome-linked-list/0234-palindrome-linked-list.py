# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        while temp is not None:
            front = temp.next    # Store next node
            temp.next = prev     # Reverse the link
            prev = temp          # Move prev forward
            temp = front         # Move temp forward
        return prev             # Return new head of reversed list

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True         # Empty list or single node is palindrome
        
        slow = head
        fast = head
        
        # Find the middle of the linked list
        while fast.next and fast.next.next:
            slow = slow.next        # Move slow 1 step
            fast = fast.next.next   # Move fast 2 steps
        
        # Reverse the second half
        new_head = self.reverseList(slow.next)
        
        # Compare first half with reversed second half
        first = head
        second = new_head
        while second is not None:
            if first.val != second.val:
                return False    # Values don't match
            first = first.next
            second = second.next
        
        # Restore original list structure (optional)
        self.reverseList(new_head)
        return True
