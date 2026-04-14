class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copyMap = {}

        node = head
        while node:
            copyMap[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            copyMap[node].next = copyMap.get(node.next)
            copyMap[node].random = copyMap.get(node.random)
            node = node.next

        return copyMap[head]
