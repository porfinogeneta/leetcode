# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        idea: robimy dwa pointery slow i fast, Turtoise&Hare algorithm
        """
        if head == None or head.next == None or head.next.next == None:
            return False
        s, f = head, head.next.next
        while s != f:
            s = s.next
            # pointer arrived at the tail, no cycle then
            if f == None or f.next == None:
                return False
            f = f.next.next
            
        return True
        