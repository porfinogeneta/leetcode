def copyRandomList( head):

    # None ma się haszować do None, jako wskaźnik
    oldToCpy = {None: None}

    cur = head
    # przechodzimy raz, zapisujemy nody w haszmapie,
    # tworzymy ich głębokie kopie
    while cur:
        newNode = Node(cur.val)
        oldToCpy[cur] = newNode
        cur = cur.next

    # wykorzystując haszmapę odtwarzamy listę
    cpy = head
    while cpy:
        node = oldToCpy[cpy]
        node.next = oldToCpy[cpy.next]
        node.random = oldToCpy[cpy.random]
        cpy = cpy.next

    return oldToCpy[head]

    # slow = head
    # fast = head
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #     if slow == fast:
    #         return True
    #
    # return False