# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        length = 0
        if head is None:
            return
        while ptr is not None:
            ptr=ptr.next
            length+=1
        ptr=head
        for i in range(length//2):
            ptr=ptr.next
        return ptr
