# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        else:
            l1 = self.mergeKLists(lists[:len(lists)//2])
            l2 = self.mergeKLists(lists[len(lists)//2:])
            result = self.mergeTwoLists(l1,l2)
            return result
        
        
        
    def mergeTwoLists(self, l1, l2):
        head = cur = ListNode(0)
        if not l1 and not l2:
            return l1 or l2
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 is None:
            cur.next = l2
        else:
            cur.next = l1
        return head.next
