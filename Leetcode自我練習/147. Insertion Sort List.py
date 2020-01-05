# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        temp = []
        node = head
        while node != None:
            temp.append(node.val)
            node = node.next
        temp.sort()
        node = head
        for n in temp:
            node.val = n
            node = node.next
        return head
        
