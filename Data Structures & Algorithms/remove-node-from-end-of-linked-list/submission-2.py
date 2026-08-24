# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        if not head.next:
            return None
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        slow = prev
        while fast:
            slow = slow.next
            fast = fast.next
        temp = slow.next.next
        slow.next = temp
        return prev.next