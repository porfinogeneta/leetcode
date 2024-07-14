def mergeTwoLists(self, l1, l2):
    dummy = ListNode()
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1: cur.next = l1
    if l2: cur.next = l2

    return dummy.next


def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists or len(lists) == 0:
        return None
    elif len(lists) == 1:
        return lists[0]
    elif len(lists) == 2:
        return self.mergeTwoLists(lists[0], lists[1])
    else:
        l1 = self.mergeKLists(lists[:len(lists) // 2])
        l2 = self.mergeKLists(lists[len(lists) // 2:])
        return self.mergeTwoLists(l1, l2)
    return lists[0]