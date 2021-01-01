# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        dummy_node = l3
        while True:
            if l1 is None:
                dummy_node.next = l2
                break
            if l2 is None:
                dummy_node.next = l1
                break
            
            if l1.val <= l2.val:
                dummy_node.next = l1
                l1 = l1.next
            else:
                dummy_node.next = l2
                l2 = l2.next
            dummy_node = dummy_node.next
        return l3.next
