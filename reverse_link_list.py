def reverse_link_list(head):

    if head is None:
        return

    reversed_head = LinkListNode(0)
    cur = head
    while cur is not None:
        tmp = cur.next
        # get cur and put at first position of reversed_list
        cur.next = reversed_head.next
        reversed_head.next = cur
        cur = tmp

    return reversed_head.next

