def reverse_stack(stack):
    if len(stack) == 0:
        return
    val = stack[-1]
    stack.pop()
    reverse_stack(stack)
    print val

stack = [1,2,3,4,5,6,7]

reverse_stack(stack)