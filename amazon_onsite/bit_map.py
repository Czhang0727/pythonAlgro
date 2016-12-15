val = 12345

while val > 0:
    val = val & (val - 1)
    print "{0:b}".format(val)
    print val