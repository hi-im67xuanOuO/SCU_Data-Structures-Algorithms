class ListNode:
    def __init__(self, x): # 定義好linked list的格式
         self.val = x
         self.next = None
class Solution(object):
    def sortList(self, head: ListNode) -> ListNode:
      
        if not head or not head.next: # 若head或head的下一個為空值，則直接return head
            return head
            
        slow = fast = head # 找出中心點
        
        while fast and fast.next:
            pre = slow # pre暫存較左的點
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        
        return self.merge(self.sortList(head), self.sortList(slow))
        
        
    def merge(self, left, right):
        res = cur = ListNode(0) # 創建一個新的linked list儲存已merge好的資料
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
