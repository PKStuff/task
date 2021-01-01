# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        total_nodes = 0
        while temp != None:
            total_nodes+=1
            temp = temp.next
        temp = head
        prev = None
        i = 0
        if (total_nodes < n):
            return -1
        while i < (total_nodes - n):
            prev = temp
            temp = temp.next
            i+=1
        if temp == head:
            del_temp = temp
            if temp.next == None:
                head = None
            else:
                temp = temp.next
                head = temp
            del del_temp
        else:
            del_temp = temp
            if temp.next == None:
                prev.next = None
            else:
                prev.next = temp.next
            del del_temp
        return head
