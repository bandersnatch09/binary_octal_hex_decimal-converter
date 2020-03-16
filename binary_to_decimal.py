def binary_to_decimal(binary):
    bi_list = []
    decimal = 0
    for x in str(binary):
        bi_list.insert(0, int(x))
    for x in range(len(bi_list)):
        if bi_list[x] == 1:
            decimal += 2 ** x
    return decimal
