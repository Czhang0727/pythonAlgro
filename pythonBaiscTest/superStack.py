class stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)
        return self.getBack()
        

    def pop(self):
        self.data.pop()
        if len(self.data) ==0:
            return "EMPTY"
        else:
            return self.getBack()
    
    def inc(self, x, val):
        for i in range(x):
            self.data[i] += val
        return self.getBack()

    def getBack(self):
        return self.data[-1]



commandsNum = int(raw_input())
myStack = stack()
for i in range(commandsNum):
    command = raw_input().split(" ")
    if command[0].lower() == "push":
        print myStack.push(int(command[1]))
    elif command[0].lower() == "pop":
        print myStack.pop()
    elif command[0].lower() == "inc":
        print myStack.inc(int(command[1]), int(command[2]))
    print myStack.data


