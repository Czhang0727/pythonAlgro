def is_power_2(val):
    
    val = (val) & (val -1)
    return val == 0

print is_power_2(3)