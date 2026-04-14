# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        node1 = head
        node2 = prev
        counter = 0
        while node1 and node2:
            if counter % 2 == 0:
                print(node2.val)
                temp = node1.next
                node1.next = node2
                node1 = temp
            else:
                print(node1.val)
                temp = node2.next
                node2.next = node1
                node2 = temp
            counter += 1
        
        
