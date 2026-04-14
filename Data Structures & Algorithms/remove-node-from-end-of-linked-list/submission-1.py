# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        count = 0
        while cur:
            length += 1
            cur = cur.next
        cur = head
        prev = head
        if length - n == 0:
            return head.next
        while cur:
            if count + 1 == length - n:
                cur.next = cur.next.next
                break
            count += 1
            cur = cur.next
        return head
