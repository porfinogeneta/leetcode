def reverseKGroup(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    dummy = ListNode(0, head)
    groupPrev = dummy
    while True:
        kth = self.getKth(groupPrev, k)
        if not kth: break
        groupNext = kth.next
        # reverse list
        prev = kth.next
        cur = groupPrev.next
        while cur != groupNext:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # podłączamy poprzednią grupę do końca aktualnej
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next


def getKth(self, cur, k):
    while cur and k > 0:
        cur = cur.next
        k -= 1
    return cur