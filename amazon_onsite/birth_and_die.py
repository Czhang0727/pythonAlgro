def birth_and_die(data):
    min_birth = min([x[0] for x in data])
    max_dead = max([x[1] for x in data])

    record = [0] * (max_dead - min_birth + 1) 

    for val in data:
        record[val[0] - min_birth] += 1
        record[val[1] - min_birth] -= 1
    

    print record
    cur_sum = 0
    max_sum = 0
    max_index = 0
    for index, val in enumerate(record):
        cur_sum += val
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_index = index
    return max_sum, max_index + min_birth


def sort_by_birth(val1,val2):
    return 1 if val1[0] > val2[0] else -1

def sort_by_death(val1, val2):
    return 1 if val1[1] > val2[1] else -1

def birth_and_die2(data):
    
    # represent begin, end, numbers of people alive
    max_times = [0,0,0]

    data.sort(sort_by_birth) 
    sorted_birth = [ x[0] for x in data]
    data.sort(sort_by_death)
    sorted_death = [ x[1] for x in data]

    cur_times = [0,sorted_death[0],0]

    while len(sorted_birth) > 0:

        if sorted_birth[0] < sorted_death[0]:
            cur_times[0] = sorted_birth[0]
            cur_times[2] += 1
            sorted_birth.pop(0)
        else:
            cur_times[1] = sorted_death[0]
            cur_times[2] -= 1
            sorted_death.pop(0) 
        
        if max_times[2] < cur_times[2]:
            max_times = list(cur_times)
        
    return max_times


data = [[1990,2005],[1994,2002],[1992,1997],[1998,2015],[1991,2003],[1987,2023],[1945,2005],[1970,2012]]

print birth_and_die2(data)

