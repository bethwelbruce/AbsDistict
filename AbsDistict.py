def solution(A):
    c=1
    mymax = max(abs(A[0]), abs(A[-1]))
    index_head = 0
    index_tail = len(A) - 1
    while index_head <= index_tail:
        head = abs(A[index_head])
        if head == mymax:
            index_head += 1
            continue
        tail = abs(A[index_tail])
        if tail == mymax:
            index_tail -= 1
            continue
        if head >= tail:
            mymax = head
            index_head += 1
        else:
            mymax = tail
            index_tail -= 1
        c += 1
    return c
    pass
