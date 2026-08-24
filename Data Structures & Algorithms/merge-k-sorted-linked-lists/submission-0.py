# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        curr1 = list1
        curr2 = list2
        curr = ListNode()
        head = curr

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = ListNode(curr1.val)
                curr = curr.next
                if curr1:
                    curr1 = curr1.next
            elif curr1.val > curr2.val:
                curr.next = ListNode(curr2.val)
                curr = curr.next
                if curr2:
                    curr2 = curr2.next
            else:
                new = ListNode()
                new.val = curr1.val
                curr.next = ListNode(curr2.val)
                curr.next.next = new
                curr = new
                if curr1:
                    curr1 = curr1.next
                if curr2:
                    curr2 = curr2.next
        
        while curr1:
            curr.next = ListNode(curr1.val)
            curr1 = curr1.next
            curr = curr.next
        while curr2:
            curr.next = ListNode(curr2.val)
            curr2 = curr2.next
            curr = curr.next
        return head.next



    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        for i in range (1,len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i-1])
        
        return lists[-1]