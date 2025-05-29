from tkinter import *
import tkinter as TK

#cores 

cor1 = "#000000"
cor2 = "#feffff"
cor3 = "#38576B"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela = Tk()
janela.title("DECISOR")
janela.geometry("235x318")
janela.resizable(False, False)
janela.config(bg="#000000")

#frames

Frame_tela = Frame(janela, width=235, height=50, bg=cor3)
Frame_tela.grid(row=0, column=0)

Frame_corpo= Frame(janela,width=235, height=268)
Frame_corpo.grid(row=1, column=0) 

#criando os botões

b_1= Button(Frame_corpo,text="C",width= 11, height=2, bg=cor4, font=("Ivy 13 bold"), fg=cor1, command=lambda: print("Limpar"))
b_1.place(x=0, y=0)
b_2= Button(Frame_corpo,text="%",width= 5, height=2 ,bg= cor5, font=("Ivy 13 bold"), fg=cor1, command=lambda: print("Porcentagem"))
b_2.place(x=118, y=0)
b_3 = Button(Frame_corpo, text="/", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), fg=cor1, command=lambda: print("Divisão"))    
b_3.place(x=177, y=0)
b_4  = Button(Frame_corpo, text="7", width=5, height=2, bg=cor2, font=("Ivy 13 bold"), fg=cor1, command=lambda: print("7"))
b_4.place(x=0, y=52)

janela.mainloop()


