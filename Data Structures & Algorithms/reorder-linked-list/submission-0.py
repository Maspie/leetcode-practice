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

        
        tmp = slow.next
        prev = None
        slow.next = None
    
        while tmp:

            temp = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = temp

        
        l1, l2 = head, prev

        while l1 and l2:

            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2

    

            

        

            
            


