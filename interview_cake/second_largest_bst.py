def largest_bst(root):
    parent = None
    n = root
    while n.right:
        parent = n
        n = n.right

    return (n, parent)

def second_largest(root):
    n, parent = largest_bst(root)
    if n.left:
        n2 = largest_bst(n.left)
        return max(n2.value, parent.value)

    return parent.value
