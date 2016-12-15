is_valid = True
last_value = None

def validation(root):
    if root is None；
        return
    
    validation(root.left)
    if last_value >= root.val

    validation(root.right)


def is_valid_bst(root):
    validation()
    return last_value