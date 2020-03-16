class hd:
    def __init__(self):
        self.hd_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, \
                        '5':5, '6':6, '7':7, '8':8, \
                        '9':9, 'A':10, 'B':11, 'C':12, \
                        'D':13, 'E':14, 'F':15}
        self.dh_dict = {}
        for x, y in self.hd_dict.items():
            self.dh_dict[y] = x
    def hex_to_decimal(self, hex):
        hex_list = [x for x in str(hex)]
        hex_list.reverse()
        decimal = 0
        for x in range(len(hex_list)):
            decimal += self.hd_dict[hex_list[x]] * 16**x
        return decimal
        
    
    def decimal_to_hex(self, decimal):
        decimal = int(decimal)
        hex = ''
        while decimal >= 16:
            hex = self.dh_dict[decimal % 16] + hex
            decimal = decimal // 16
        hex = self.dh_dict[decimal] + hex
        return hex
            
