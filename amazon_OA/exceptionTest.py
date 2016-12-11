
try:
    val = int(raw_input("Enter a number:"))
except ValueError as e:
    print "Invalid number:",e