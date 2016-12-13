
def recur_reverse(data):
    if len(data) == 0:
        return data
    data[0],data[-1] = data[-1],data[0]
    data[1:-1] = recur_reverse(data[1:len(data)-1])
    return data

def reverse(data):
    data = data.split(" ")
    return recur_reverse(data)



data = "I am a cat"
print reverse(data)