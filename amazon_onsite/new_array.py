def create_new_array(arr_a, arr_b):
    data_set = set()
    for val in arr_b:
        if val in data_set:
            pass
        else:
            data_set.add(val)

    res = filter(lambda x: x not in data_set, arr_a)
    return res

print create_new_array([1,1,1,1,2,3,4],[1])

