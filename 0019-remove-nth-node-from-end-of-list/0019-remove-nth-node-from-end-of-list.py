# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==0:
            return head
        temp=head
        count=0

        while temp is not None:
            count+=1
            temp=temp.next
        if count==n:
            head=head.next
            return head
        i=1
        temp=head
        while i<count-n:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        return head

        