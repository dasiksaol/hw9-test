import math
import os


def binary_con(opt, value):
    
    '''
    @param opt: 'bd' or 'db', binary to decimal or decimal to binary
    @param value: the value to be converted, integer
    @return: the converted value

    example binary_con('bd', 1001) should return 9 as int value, and binary_con('db', 8) should return 1000 as int.
    '''
    if opt == "db":
        if value >= 2:
            result = ""
            while value >= 2:
                    remainder = value % 2 
                    result += str(remainder)
                    value = value // 2
                    if value < 2:
                        result += str(value)
            return int(result[::-1])
        elif value in [0, 1]:
             return value
    elif opt == "bd":
        for x in str(value):
            if x not in ["0", '1']:
                return "Error: Invalid Number"
        else:
            result = 0
            value = str(value)[::-1]
            for index, x in enumerate(value):
                result += ( (2**index) * int(x) )
            return result


# print(binary_con("bd", 10010001))
# print(binary_con("db", 145))





