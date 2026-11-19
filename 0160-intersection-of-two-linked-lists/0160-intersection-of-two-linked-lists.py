# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        all_nodes = set()  # Set to store all nodes from first list
        temp = headA
        
        # First pass: Store all nodes from list A
        while temp:
            all_nodes.add(temp)  # Add current node to set
            temp = temp.next
        
        temp = headB
        
        # Second pass: Check each node of list B in the set
        while temp:
            if temp in all_nodes:  # Found intersection!
                return temp
            temp = temp.next
        
        return None  # No intersection found