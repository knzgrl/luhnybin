DIGITS = ['0','1','2','3','4','5','6','7','8','9']
CARD_CHARS = [' ','-','0','1','2','3','4','5','6','7','8','9']

def is_luhny(x):
    str_x = str(x)
    sum = 0
    for i in range( len(str_x) - 1,-1,-2):
        sum += int(str_x[i])
    for j in range( len(str_x) - 2,-1,-2):
        double_str = str( int( str_x[j] ) * 2)
        for k in range( len(double_str) ):
            sum += int( double_str[k] )
    if sum % 10 == 0:
        return True
    return False

def are_card_chars(string):
    for i in range( len(string) ):
        if not string[i] in CARD_CHARS:
            return False
    return True

def are_numbers(string):
    for i in range( len(string) ):
        if not string[i] in DIGITS:
            return False
    return True

#def log(string):
    for i in range( len(string) ):
        if string[i] in DIGITS:

print are_numbers(raw_input())