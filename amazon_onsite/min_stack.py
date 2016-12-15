class min_stack():

    def __init__(self):
        self.data = []
        self.min_data = []

    def get_min(self):
        return self.min_data[-1]

    def top(self):
        return self.data[-1]

    def push(self, val):
        self.data.append(val)
        if len(self.min_data) == 0 or val <= self.min_data[-1]:
            self.min_data.append(val)

    def pop(self):
        removed = self.data.pop()
        if removed == self.min_data[-1]:
            self.min_data.pop()
        return removed

mystack = min_stack()
mystack.push(3)
mystack.push(1)
mystack.push(5)

print mystack.get_min()
print mystack.top()

