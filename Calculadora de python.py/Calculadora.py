from tkinter import *
import tkinter as ttk

janela = Tk()

#cores 

cor1 = "#000000"
cor2 = "#feffff"
cor3 = "#38576B"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela = Tk(), 
janela.title("decisor")
janela.geometry("235x268")
janela.config(bg=cor1)

#frames

Frame_tela = Frame(janela, width=235, height=50, bg=cor3)
Frame_tela.grid(row=0, column=0)

Frame_corpo= Frame(janela,width=235, height=268)
Frame_corpo.grid(row=1, column=0) 

#criando os botões

b_1= Button(Frame_corpo,text="C",width= 20, height=2, bg=cor4 )
b_1.place(x=0, y=0)
b_2= Button(Frame_corpo,text="%",width= 5, height=2 ,bg= cor5)
b_2.place(x=120, y=0)
b_3 = Button(Frame_corpo, text="/", width=5, height=2, bg=cor5)
b_3.place(x=180, y=0)


janela.mainloop()


