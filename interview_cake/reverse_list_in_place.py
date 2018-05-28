def reverse(n):
    prev = None

    while n is not None:
        temp = n.next
        n.next = prev
        prev = n
        n = temp

    return prev