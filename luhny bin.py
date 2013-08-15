def sum(int_list):
    sum = 0
    for item in int_list:
        sum += int(item)
    return sum

def slice(list):
    sliced_list = []
    for item in list:
        for i in range(len(str(item))):
            sliced_list.append(str(item)[i])
    return sliced_list

def is_luhny(x):
    list_x = list(str(x))
    for i in range(len(list_x)-2,-1,-2):     # double every other digit from the right skipping the far right
        list_x[i] = int(list_x[i]) * 2
    if sum(slice(list_x)) % 10 == 0:
        return True
    return False

print is_luhny(5678)
print is_luhny(6789)