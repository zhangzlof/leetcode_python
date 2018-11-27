# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while (cur and count!=k):
            cur = cur.next
            count += 1
            
        if (count==k):
            cur =self.reverseKGroup(cur,k);
            while(count>0):
                temp =head.next
                head.next=cur #将head指向cur
                cur=head  #将cur向前移动一位
                head=temp #将head向后移动一位
                count = count - 1
            head=cur
        return head
            
            
            
           
            
    
        
