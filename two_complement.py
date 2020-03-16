from addition import*
from one_complement import*
from subtraction import*

def two_complement(decimal):
    one_binary = one_complement(decimal)
    return binary_addition(str(one_binary) + ',1')

def two_complement_8(decimal):
    one_binary = one_complement_8(decimal)
    return binary_addition(str(one_binary) + ',1')

def two_complement_16(decimal):
    one_binary = one_complement_16(decimal)
    return binary_addition(str(one_binary) + ',1')

def two_to_decimal(two_complement):
    one_complement = binary_subtraction(str(two_complement) + ',1')
    decimal = one_to_decimal(one_complement)
    return decimal
