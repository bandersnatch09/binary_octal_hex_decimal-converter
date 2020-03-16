from octal_decimal import*
from hex_decimal import*

def binary_addition(nums):
    point = str(nums).find(',')
    b1 = str(nums)[:point].strip()
    b2 = str(nums)[point+1:].strip()
    length1 = len(str(b1))
    length2 = len(str(b2))
    result = ''
    if length1 > length2:
        b2 = '0'*(length1-length2) + str(b2)
    else:
        b1 = '0'*(length2-length1) + str(b1)
    b1, b2 = str(b1), str(b2)
    extra = False
    for x in range(len(b1)-1, -1, -1):
        if b1[x] == '1' and b2[x] == '1':
            if not extra:
                result = '0' + result
                extra = True
            else:
                result = '1' + result
                

        elif b1[x] == '0' and b2[x] == '0':
            if not extra:
                result = '0' + result
            else:
                result = '1' + result
                extra = False
        else:
            if not extra:
                result = '1' + result
            else:
                result = '0' + result
    if extra:
        result = '1'+result
    return result

def octal_addition(nums):
    point = str(nums).find(',')
    o1 = str(nums)[:point].strip()
    o2 = str(nums)[point+1:].strip()

    d1 = octal_to_decimal(o1)
    d2 = octal_to_decimal(o2)

    return decimal_to_octal(d1+d2)

def hex_addition(nums):
    h_d = hd()
    point = str(nums).find(',')
    h1 = str(nums)[:point].strip()
    h2 = str(nums)[point+1:].strip()
    d1 = h_d.hex_to_decimal(h1)
    d2 = h_d.hex_to_decimal(h2)
    return h_d.decimal_to_hex(d1+d2)

    
