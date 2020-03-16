import tkinter
from tkinter import*
from tkinter.messagebox import*
from decimal_to_binary import*
from binary_to_decimal import*
from one_complement import*
from two_complement import*
from fraction_to_binary import*
from addition import*
from octal_decimal import*
from hex_decimal import*
from subtraction import*
class GUI_Function:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("cs110 A1")
        self.root.geometry('500x300')
        self.input = Frame(self.root)
        self.output = Frame(self.root)
        self.input.pack()
        self.output.pack()
        self.entry1 = StringVar()
        self.entry2 = StringVar()
        self.entry3 = StringVar()
        self.entry4 = StringVar()
        self.entry5 = StringVar()
        self.entry6 = StringVar()
        self.entry7 = StringVar()
        self.entry8 = StringVar()
        #create option button
        self.option1 = StringVar()
        self.option1.set("decimal to binary")
        option_d_b = OptionMenu(self.input, self.option1, "decimal to binary", "8-bits", "16-bits").grid(row=1, stick=W)
        entry_d_b = Entry(self.input, textvariable=self.entry1).grid(row=1, column=1, stick=E)
        button_d_b = Button(self.input, text="run", command=self.d_to_b).grid(row=1, column=2, stick=E)

        label_b_d = Label(self.input, text="binary to decimal").grid(row=2, stick=W)
        entry_b_d = Entry(self.input, textvariable=self.entry2).grid(row=2, column=1, stick=E)
        button_b_d = Button(self.input, text="run", command=self.b_to_d).grid(row=2, column=2)

        self.option3 = StringVar()
        self.option3.set("one's complement")
        option_one = OptionMenu(self.input, self.option3,"one's complement", "8-bits", "16-bits", "one_to_decimal").grid(row=3, stick=W)
        entry_one = Entry(self.input, textvariable=self.entry3).grid(row=3, column=1, stick=E)
        button_one = Button(self.input, text="run", command=self.one).grid(row=3, column=2)
        
        self.option4 = StringVar()
        self.option4.set("two's complement")
        option_two = OptionMenu(self.input, self.option4, "two's complement", "8-bits", "16-bits", "two_to_decimal").grid(row=4, stick=W)
        entry_two = Entry(self.input, textvariable=self.entry4).grid(row=4, column=1, stick=E)
        button_two = Button(self.input, text="run", command=self.two).grid(row=4, column=2)


        self.option5 = StringVar()
        self.option5.set("binary_addition")
        option_addition = OptionMenu(self.input, self.option5, "binary_addition", "octal_addition", "hex_addition").grid(row=5, stick=W)
        entry_addition = Entry(self.input, textvariable=self.entry5).grid(row=5, column=1, stick=E)
        button_addition = Button(self.input, text="run", command=self.addition).grid(row=5, column=2)

        self.option6 = StringVar()
        self.option6.set("octal_to_decimal")
        option_o_d = OptionMenu(self.input, self.option6, "octal_to_decimal", "decimal_to_octal").grid(row=6, stick=W)
        entry_o_d = Entry(self.input, textvariable=self.entry6).grid(row=6, column=1, stick=E)
        button_o_d = Button(self.input, text="run", command=self.o_d).grid(row=6, column=2)


        self.option7 = StringVar()
        self.option7.set("hex_to_decimal")
        option_h_d = OptionMenu(self.input, self.option7, "hex_to_decimal", "decimal_to_hex").grid(row=7, stick=W)
        entry_h_d = Entry(self.input, textvariable=self.entry7).grid(row=7, column=1, stick=E)
        button_h_d = Button(self.input, text="run", command=self.h_d).grid(row=7, column=2)

        self.option8 = StringVar()
        self.option8.set("binary_subtraction")
        option_subtraction = OptionMenu(self.input, self.option8, "binary_subtraction", "octal_subtraction", "hex_subtraction").grid(row=8, stick=W)
        entry_subtraction = Entry(self.input, textvariable=self.entry8).grid(row=8, column=1, stick=E)
        button_subtraction = Button(self.input, text="run", command=self.subtraction).grid(row=8, column=2)


        #output frame
        self.display_info = tkinter.Listbox(self.output, width=80)
        self.display_info.grid()

    def d_to_b(self):
        if self.option1.get() == "decimal to binary":
            b = decimal_to_binary(self.entry1.get())
        elif self.option1.get() == "8-bits":
            b = decimal_to_binary_8(self.entry1.get())
        elif self.option1.get() == "16-bits":
            b = decimal_to_binary_16(self.entry1.get())
        self.display_info.delete(0, 'end')
        self.display_info.insert(0, 'if decimal is negative, the first 0 shoud be 1')
        self.display_info.insert(0, b)
        
    def b_to_d(self):
        d = binary_to_decimal(self.entry2.get())
        self.display_info.delete(0, 'end')
        self.display_info.insert(0, d)
        
    def one(self):
        if self.option3.get() == "one's complement":
            one = one_complement(self.entry3.get())
        elif self.option3.get() == "8-bits":
            one = one_complement_8(self.entry3.get())
        elif self.option3.get() == "16-bits":
            one = one_complement_16(self.entry3.get())
        elif self.option3.get() == "one_to_decimal":
            one = one_to_decimal(self.entry3.get())
        self.display_info.delete(0, 'end')
        self.display_info.insert(0, one)
        
    def two(self):
        if self.option4.get() == "two's complement":
            two = two_complement(self.entry4.get())
        elif self.option4.get() == "8-bits":
            two = two_complement_8(self.entry4.get())
        elif self.option4.get() == "16-bits":
            two = two_complement_16(self.entry4.get())
        elif self.option4.get() == "two_to_decimal":
            two = two_to_decimal(self.entry4.get())
        self.display_info.delete(0, 'end')
        self.display_info.insert(0, two)
        
    def addition(self):
        if self.option5.get() == "binary_addition":
            result = binary_addition(self.entry5.get())
        elif self.option5.get() == "octal_addition":
            result = octal_addition(self.entry5.get())
        elif self.option5.get() == "hex_addition":
            result = hex_addition(self.entry5.get())
        self.display_info.delete(0, 'end')
        self.display_info.insert(0, result)

    def o_d(self):
        if self.option6.get() == "octal_to_decimal":
            r_od = octal_to_decimal(self.entry6.get())
        elif self.option6.get() == "decimal_to_octal":
            r_od = decimal_to_octal(self.entry6.get())
        self.display_info.delete(0, 'end')
        self.display_info.insert(0, r_od)

    def h_d(self):
        h_d = hd()
        if self.option7.get() == "hex_to_decimal":
            r_hd = h_d.hex_to_decimal(self.entry7.get())
        elif self.option7.get() == "decimal_to_hex":
            r_hd = h_d.decimal_to_hex(self.entry7.get())
        self.display_info.delete(0, 'end')
        self.display_info.insert(0, r_hd)

    def subtraction(self):
        if self.option8.get() == "binary_subtraction":
            result = binary_subtraction(self.entry8.get())
        elif self.option8.get() == "octal_subtraction":
            result = octal_subtraction(self.entry8.get())
        elif self.option8.get() == "hex_subtraction":
            result = hex_subtraction(self.entry8.get())
        self.display_info.delete(0, 'end')
        self.display_info.insert(0, result)
