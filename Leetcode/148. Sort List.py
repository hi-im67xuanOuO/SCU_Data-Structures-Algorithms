#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def sortList(self, head: ListNode) -> ListNode:
        
        #A intuitive solution but may be not constant space
        if not head or not head.next:
            return head #just like the array merge-sort
        # pre = ListNode(0) #use it to clear the rear half linked list
        slow = fast = head #find the mid point
        while fast and fast.next: #A normal way to go through the linked list using 2 pointer.
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        
        return self.merge(self.sortList(head), self.sortList(slow))
        
        
    def merge(self, left, right): #just like the mergesort in array, we need to merge each time
        res = cur = ListNode(0) #created a new linked list to keep the merge
        while left and right:
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next
            if left: 
                cur.next = left
            if right: 
                cur.next = right
        return res.next
