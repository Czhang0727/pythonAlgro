def isAlpha(c):
    if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
        return True
    return False

def first_repeat_word(word):

    visited = set()
    for c in word:
        if isAlpha(c):
            if c in visited:
                return c
            else:
                visited.add(c)
    return -1

print first_repeat_word("DSFHI:JK:")