from tkinter import Tk, Entry, Button, END


class Calculator(Tk):
    def __init__(self):
        super().__init__()
        # Creacion de ventana y entrada de valores
        self.input_text = Entry(self, font="Calibri 20")

        # Números a botones
        self.button_1 = Button(self, text='1', width=5, height=2, command=lambda: self.click_button(1))
        self.button_2 = Button(self, text='2', width=5, height=2, command=lambda: self.click_button(2))
        self.button_3 = Button(self, text='3', width=5, height=2, command=lambda: self.click_button(3))
        self.button_4 = Button(self, text='4', width=5, height=2, command=lambda: self.click_button(4))
        self.button_5 = Button(self, text='5', width=5, height=2, command=lambda: self.click_button(5))
        self.button_6 = Button(self, text='6', width=5, height=2, command=lambda: self.click_button(6))
        self.button_7 = Button(self, text='7', width=5, height=2, command=lambda: self.click_button(7))
        self.button_8 = Button(self, text='8', width=5, height=2, command=lambda: self.click_button(8))
        self.button_9 = Button(self, text='9', width=5, height=2, command=lambda: self.click_button(9))
        self.button_0 = Button(self, text='0', width=5, height=2, command=lambda: self.click_button(0))

        #  Signos de conjuncion a botones
        self.button_delete = Button(self, text='AC', width=5, height=2, command=lambda: self.click_delete())
        self.button_bracketL = Button(self, text='(', width=5, height=2, command=lambda: self.click_button('('))
        self.button_bracketR = Button(self, text=')', width=5, height=2, command=lambda: self.click_button(')'))
        self.button_dot = Button(self, text='.', width=5, height=2, command=lambda: self.click_button('.'))

        # Signos de operación a botones
        self.button_div = Button(self, text='/', width=5, height=2, command=lambda: self.click_button('/'))
        self.button_mul = Button(self, text='*', width=5, height=2, command=lambda: self.click_button('*'))
        self.button_add = Button(self, text='+', width=5, height=2, command=lambda: self.click_button('+'))
        self.button_sub = Button(self, text='-', width=5, height=2, command=lambda: self.click_button('-'))
        self.button_equal = Button(self, text='=', width=5, height=2, command=lambda: self.click_equal())

        # Se establecen en dónde va a estar ubicado cada elemento
        self.set_value_window()

    def set_value_window(self): # Colocado de los elementos en la ventana
        self.title('Calculadora')
        self.input_text.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.button_delete.grid(row=1, column=0, padx=5, pady=5)
        self.button_bracketL.grid(row=1, column=1, padx=5, pady=5)
        self.button_bracketR.grid(row=1, column=2, padx=5, pady=5)
        self.button_div.grid(row=1, column=3, padx=5, pady=5)

        self.button_7.grid(row=2, column=0, padx=5, pady=5)
        self.button_8.grid(row=2, column=1, padx=5, pady=5)
        self.button_9.grid(row=2, column=2, padx=5, pady=5)
        self.button_mul.grid(row=2, column=3, padx=5, pady=5)

        self.button_4.grid(row=3, column=0, padx=5, pady=5)
        self.button_5.grid(row=3, column=1, padx=5, pady=5)
        self.button_6.grid(row=3, column=2, padx=5, pady=5)
        self.button_add.grid(row=3, column=3, padx=5, pady=5)

        self.button_1.grid(row=4, column=0, padx=5, pady=5)
        self.button_2.grid(row=4, column=1, padx=5, pady=5)
        self.button_3.grid(row=4, column=2, padx=5, pady=5)
        self.button_sub.grid(row=4, column=3, padx=5, pady=5)

        self.button_0.grid(row=5, column=0, padx=5, pady=5)
        self.button_dot.grid(row=5, column=1, padx=5, pady=5)
        self.button_equal.grid(row=5, column=2, padx=5, pady=5)

    def click_button(self, val):
        self.input_text.insert(END, val)

    def click_delete(self):
        self.input_text.delete(0, END)

    def click_equal(self):
        ec = self.input_text.get()
        res = str(eval(ec))
        self.input_text.delete(0, END)
        self.input_text.insert(0, res)
