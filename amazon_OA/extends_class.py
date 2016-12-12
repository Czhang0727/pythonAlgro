class A:
    def __init__(self):
        print "I am A"

    def print_me(self):
        print "HHA"

class B(A):

    def __init__(self):
        print "I am B"

    def print_me(self):
        print "wahaha"


obj = B()
obj.print_me()