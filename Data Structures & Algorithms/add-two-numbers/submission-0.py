# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        cur = node
        ones = 0
        tens = 0
        while l1 or l2 or tens:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + tens
            ones = val % 10
            tens = val // 10
            cur.next = ListNode(ones)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return node.next