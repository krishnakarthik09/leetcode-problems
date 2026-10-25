# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None or k==0:
            return head
        fast=head
        slow=head
        curr=head
        length=0
        while curr:
            curr=curr.next
            length+=1
        k=k%length
        if k==0:
            return head
        while k>0:
            fast=fast.next
            k-=1
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        front=slow.next
        slow.next=None
        fast.next=head
        return front
        



        


        