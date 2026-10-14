# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode(0,head)

        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        stepstomove=length-n
        curr=dummy
        for _ in range(stepstomove):
            curr=curr.next
        curr.next=curr.next.next

        return dummy.next
        

            


        