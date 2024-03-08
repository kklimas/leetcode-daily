def middle_node(head):
    n = 0
    body = head
    while body is not None:
        body = body.next
        n += 1

    n //= 2
    body = head
    while n > 0:
        body = body.next
        n -= 1
    return body
