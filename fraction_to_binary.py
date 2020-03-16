def frac_to_binary(decimal_frac):
    binary = ''
    flo = decimal_frac
    while flo != 0 and len(binary) <= 10:
        flo = flo * 2
        integer = str(int(flo))
        flo  = float('0' + str(flo)[str(flo).find('.'):])
        binary += integer
    binary = '0.' + binary
    return binary

