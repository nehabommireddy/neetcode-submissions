# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        #find midpoint
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse second half
        curr = slow.next
        slow.next = None
        prev = None       
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        #merge second half with first half  
        curr2 = prev 
        head2 = head
        while curr2:
            head2_temp = head2.next
            curr2_temp = curr2.next

            head2.next = curr2
            curr2.next = head2_temp

            curr2 = curr2_temp
            head2 = head2_temp

          