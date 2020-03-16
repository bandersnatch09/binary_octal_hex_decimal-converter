from binary_to_decimal import*
from decimal_to_binary import*
from octal_decimal import*
from hex_decimal import*


def binary_subtraction(nums): #must be b1 - b2
    point = str(nums).find(',')
    b1 = str(nums)[:point].strip()
    b2 = str(nums)[point+1:].strip()
    b1, b2 = str(b1), str(b2)
    d1, d2 = binary_to_decimal(b1), binary_to_decimal(b2)
    sub_result = d1 - d2
    return '0'*(len(b1)-len(decimal_to_binary(sub_result))) + decimal_to_binary(sub_result)

def octal_subtraction(nums):
    point = str(nums).find(',')
    o1 = str(nums)[:point].strip()
    o2 = str(nums)[point+1:].strip()
    d1, d2 = octal_to_decimal(o1), octal_to_decimal(o2)
    return decimal_to_octal(d1-d2)

def hex_subtraction(nums):
    h_d = hd()
    point = str(nums).find(',')
    h1 = str(nums)[:point].strip()
    h2 = str(nums)[point+1:].strip()
    d1 = h_d.hex_to_decimal(h1)
    d2 = h_d.hex_to_decimal(h2)
    return h_d.decimal_to_hex(d1-d2)

