def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    idea: robimy dummy node i potem przechodząc przez dwie linked listy po kolei
    doklejamy rzewczy do dummy node'a
    """

    dummy = ListNode()
    head = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            dummy.next = ListNode(list1.val)
            list1 = list1.next
        else:
            dummy.next = ListNode(list2.val)
            list2 = list2.next
        dummy = dummy.next()

    if list1:
        dummy.next = list1
    if list2:
        dummy.next = list2

    return head.next
