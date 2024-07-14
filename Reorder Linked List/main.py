def reorderList(head):

    # dzielimy listę na pół, drugą część odwracamy i łączymy z pierwszą
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    # odwracamy drugą połówkę
    prev = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # łączymy obie listy
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2