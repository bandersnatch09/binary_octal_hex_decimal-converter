def decimal_to_binary(decimal):
    decimal = int(decimal)
    binary = ''
    while decimal != 0 and decimal != 1:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    binary = str(decimal) + binary
    return binary

def decimal_to_binary_8(decimal):
    decimal = int(decimal)
    binary = ''
    while decimal != 0 and decimal != 1:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    binary = str(decimal) + binary
    return '0'*(8-len(binary))+binary

def decimal_to_binary_16(decimal):
    decimal = int(decimal)
    binary = ''
    while decimal != 0 and decimal != 1:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    binary = str(decimal) + binary
    return '0'*(16-len(binary))+binary
