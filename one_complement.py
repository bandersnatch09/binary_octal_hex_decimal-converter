from decimal_to_binary import*
from binary_to_decimal import*

def one_complement(decimal):
    ori_binary = decimal_to_binary(decimal)
    one_binary = str(ori_binary)[0]
    for x in str(ori_binary)[1:]:
        if x == '1':
            one_binary += '0'
        else:
            one_binary += '1'
    return one_binary


def one_complement_8(decimal):
    ori_binary = decimal_to_binary_8(decimal)
    one_binary = str(ori_binary)[0]
    for x in str(ori_binary)[1:]:
        if x == '1':
            one_binary += '0'
        else:
            one_binary += '1'
    return one_binary

def one_complement_16(decimal):
    ori_binary = decimal_to_binary_16(decimal)
    one_binary = str(ori_binary)[0]
    for x in str(ori_binary)[1:]:
        if x == '1':
            one_binary += '0'
        else:
            one_binary += '1'
    return one_binary



def one_to_decimal(one_complement):
    ori_binary = ''
    for x in one_complement[1:]:
        if x == '1':
            ori_binary += '0'
        else:
            ori_binary += '1'
    decimal = binary_to_decimal(ori_binary)
    return decimal
