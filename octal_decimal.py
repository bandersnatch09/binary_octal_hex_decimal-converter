def octal_to_decimal(octal):
    octal_list = []
    decimal = 0
    for x in str(octal):
        octal_list.insert(0, x)
    for x in range(len(octal_list)):
        decimal += int(octal_list[x]) * 8**x
    return decimal

def decimal_to_octal(decimal):
    decimal = int(decimal)
    octal = ''
    while decimal >= 8:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    octal = str(decimal) + octal
    return octal

