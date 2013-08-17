import sys

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
    for i in range(len(list_x)-2,-1,-2):        # double every other digit from the right skipping the far right
        list_x[i] = int(list_x[i]) * 2
    if sum(slice(list_x)) % 10 == 0:
        return True
    return False

def log(x):
    str_x = str(x)
    log = {}                                    # key : value :: start-index : length
    for i in range(len(str_x)-13):
        for j in range(16,13,-1):
            if i+j <= len(str_x):
                if is_luhny(str_x[i:i+j]):
                    log[i] = j
                    break
    return log

def mask(x):
    str_x = str(x)
    log_x = log(x)
    for start_index in log_x:
        length = log_x[start_index]
        str_x = str_x[:start_index] + 'X'*length + str_x[start_index+length:]
    return str_x

for line in sys.stdin:
    print mask(line),