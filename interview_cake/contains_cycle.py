def contains_cycle(n):
    slow = n
    fast = n

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False