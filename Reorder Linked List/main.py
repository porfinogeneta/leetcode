def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    O(n) złożoność
    O(1) pamięć
    idea: przechodzimy slow i fast pointer żeby znaleźć drugą połowę listy,
    drugą część odwracamy i mergujemy obie listy
    """
    # to gdzie jest połowa listy dowiemy się z tego gdzie wyląduje slow pointer
    # jak będziemy listę przechodzić slow i fast pointerem
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # przekazujemy slow.next, bo chcemy, żeby second zawsze był krótszy
    second = slow.next
    slow.next = None
    prev = None
    # teraz odwracamy drugą połowkę
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
        first = tmp1
        second = tmp2