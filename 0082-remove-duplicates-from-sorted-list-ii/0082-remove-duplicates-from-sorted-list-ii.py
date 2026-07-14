# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        temp=head
        while temp is not None:
            flag=False
            front=temp.next
            while front is not None and temp.val==front.val:
                temp=front
                front=front.next
                flag=True
            if temp.val==head.val and flag:
                head=front
                temp.next=None
                temp=None
            elif flag:
                prev.next=front
                temp.next=None
                temp=None
            if temp is not None:
                prev=temp
            temp=front
        return head
    

        
