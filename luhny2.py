# STATUS: PASS
# TIMES: 389ms
#        454ms
#        383ms
#        373ms
#        370ms

import sys 

DIGITS = ['0','1','2','3','4','5','6','7','8','9']
CARD_CHARS = [' ','-','0','1','2','3','4','5','6','7','8','9']

log_errors = open('log.txt','a')

def is_luhny(x):
    str_x = str(x)
    log_errors.write('checking '+str_x+'\n')
    sum = 0
    for i in range( len(str_x) - 1,-1,-2):
#        log_errors.write( str_x[i]+': '+str( ord( str_x[i] ) )+'\n')
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

def log(string):
    num_log = {}                                        # key : value :: starting index : length
    # for non-delimited numbers
    for i in range(14,17):                              # cycle through possible lengths of card numbers
        for j in range( len(string) - i + 1):              # cycle through every possible starting digit
            if are_numbers( string[j:j+i] ):                # if those characters are all numbers
                log_errors.write('is_luhny might be called from non-delimited sequence\n')
                if is_luhny( string[j:j+i] ):                   # if those numbers pass the luhn check
                    num_log[j] = i                                      # add to log
    # yay delimiters /sarcasm
    for i in range(19,16,-1):                       # cycle through possible lengths of delimited card numbers
        j = 0
        while j <= ( len(string) - i ):
            if are_card_chars( string[j:j+i] ):             # if those characters are all numbers, spaces, or -
                if are_numbers( string[j:j+4] ):                # if the first four are numbers
                    if not (string[j+4] in DIGITS):                   # if the fifth is not
                        log_errors.write('is_luhny might be called from delimited sequence\n')
                        card_num = string[j:j+4] + string[j+5:j+9] + string[j+10:j+14] + string[j+15:j+i]
                        if not card_num[-1] in DIGITS:
                            card_num = card_num[:-1]
                        if is_luhny( card_num ):
                            num_log[j] = i-3
            j += 1
    return num_log

def mask(string):
    num_log = log(string)
    if num_log == {}:
        return string
    for start_index in num_log:
        if not (string[start_index+4] in DIGITS) and string[start_index+4] != 'X':
            string = string[:start_index] + 'XXXX' + string[start_index+4] + 'XXXX' + string[start_index+9] + 'XXXX' + string[start_index+14] + 'X' * (num_log[start_index] - 12) + string[start_index + num_log[start_index] + 3:]
        else:
            string = string[:start_index] + 'X'*num_log[start_index] + string[start_index+num_log[start_index]:]
    return string

def run():
    line = raw_input()
    while len(line) > 0:
#        log_errors.write('Input:\t'+line+'\n')
#        log_errors.write('Output:\t'+mask(line))
        print mask(line)
        try:
            line = raw_input()
        except EOFError:
            return
    log_errors.write('\n')
    log_errors.close()

run()
#print log(raw_input())