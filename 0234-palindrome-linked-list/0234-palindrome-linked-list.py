# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list1 = []
        list2 = []
        ptr=head
        while ptr:
            list1.append(ptr.val)
            ptr=ptr.next
        ptr=head
        prev=None
        while ptr:
            temp=ptr.next
            ptr.next=prev
            prev=ptr
            ptr=temp
        ptr=prev
        while ptr:
            list2.append(ptr.val)
            ptr=ptr.next
        
        if list1==list2:
            return True
        else:
            return False
            