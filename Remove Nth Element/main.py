def removeNthFromEnd( head, n):

    # mamy dwa wskaźniki, jeden na początku, drugi przesunięty o n
    # dopóki prawy (przesunięty).next != null przesuwamy
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1

    # przechodzimy dopóki prawy nie będzie pusty (koniec listy)
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next

    return dummy.next