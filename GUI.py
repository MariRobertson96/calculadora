from tkinter import Tk, Button, Entry, StringVar
from sql import sql_database

entry_expression = ''

class app(Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("215x330")
        self.resizable(width="false",height="false")
        self.expression = StringVar()
        self.screen = Entry(self, textvariable= self.expression)
        self.screen.grid(columnspan=4,rowspan=1,ipadx=45,ipady=15)
    
        #botoes
        button_sqrt = Button(self, text="sqrt", font=("Calibri",10,"bold"),
                    command=lambda: self.press("**(1/2)"),height=3,width=6)
        button_sqrt.grid(row=2,column=0)
        button_pow = Button(self, text="x^y", font=("Calibri",10,"bold"),
                    command=lambda: self.press("**"),height=3,width=6)
        button_pow.grid(row=2,column=1)
        button_percent = Button(self, text="%", font=("Calibri",10,"bold"),
                    command=lambda: self.press("*(0.01)*"),height=3,width=6)
        button_percent.grid(row=2,column=2)
        button_division = Button(self, text="/", font=("Calibri",10,"bold"),
                    command=lambda: self.press("/"),height=3,width=6)
        button_division.grid(row=2,column=3)
        button_7 = Button(self, text="7", font=("Calibri",10,"bold"),
                    command=lambda: self.press(7),height=3,width=6)
        button_7.grid(row=3,column=0)    
        button_8 = Button(self, text="8", font=("Calibri",10,"bold"),
                    command=lambda: self.press(8),height=3,width=6)
        button_8.grid(row=3,column=1) 
        button_9 = Button(self, text="9", font=("Calibri",10,"bold"),
                    command=lambda: self.press(9),height=3,width=6)
        button_9.grid(row=3,column=2) 
        button_mult = Button(self, text="*", font=("Calibri",10,"bold"),
                    command=lambda: self.press("*"),height=3,width=6)
        button_mult.grid(row=3,column=3) 
        button_4 = Button(self, text="4", font=("Calibri",10,"bold"),
                    command=lambda: self.press(4),height=3,width=6)
        button_4.grid(row=4,column=0)    
        button_5 = Button(self, text="5", font=("Calibri",10,"bold"),
                    command=lambda: self.press(5),height=3,width=6)
        button_5.grid(row=4,column=1) 
        button_6 = Button(self, text="6", font=("Calibri",10,"bold"),
                    command=lambda: self.press(6),height=3,width=6)
        button_6.grid(row=4,column=2) 
        button_sum = Button(self, text="+", font=("Calibri",10,"bold"),
                    command=lambda: self.press("+"),height=3,width=6)
        button_sum.grid(row=4,column=3) 
        button_1 = Button(self, text="1", font=("Calibri",10,"bold"),
                    command=lambda: self.press(1),height=3,width=6)
        button_1.grid(row=5,column=0)    
        button_2 = Button(self, text="2", font=("Calibri",10,"bold"),
                    command=lambda: self.press(2),height=3,width=6)
        button_2.grid(row=5,column=1) 
        button_3 = Button(self, text="3", font=("Calibri",10,"bold"),
                    command=lambda: self.press(3),height=3,width=6)
        button_3.grid(row=5,column=2) 
        button_diff = Button(self, text="-", font=("Calibri",10,"bold"),
                    command=lambda: self.press("-"),height=3,width=6)
        button_diff.grid(row=5,column=3)
        button_clear = Button(self,text="C", font=("Calibri",10,"bold"),bg="crimson",
                    command=self.clear,height=3,width=6)
        button_clear.grid(row=6,column=0)
        button_0 = Button(self, text="0", font=("Calibri",10,"bold"),
                    command=lambda: self.press(0),height=3,width=6)
        button_0.grid(row=6,column=1)
        button_decimal = Button(self, text=".", font=("Calibri",10,"bold"),
                    command=lambda: self.press("."),height=3,width=6)
        button_decimal.grid(row=6,column=2)
        button_result = Button(self,text="=", font=("Calibri",10,"bold"),bg="aquamarine1",
                    command=self.result,height=3,width=6)
        button_result.grid(row=6,column=3)

        self.mainloop()

    def press(self, number):
        global entry_expression
        entry_expression = entry_expression + str(number)
        self.expression.set(entry_expression)

    def result(self):
        try:
            global entry_expression
            save_math_operation = self.expression.get()
            total = str(eval(entry_expression))
            self.expression.set(total)
            entry_expression = ""
            sql_database().insert_table(save_math_operation,self.expression.get(),"Sucesso")
        except:
            self.expression.set("Error")
            sql_database().insert_table(save_math_operation,self.expression.get(),"Erro")
            entry_expression = ""
    
    def clear(self):
        global entry_expression
        entry_expression = ""
        self.expression.set(0)