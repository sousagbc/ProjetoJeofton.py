from tkinter import *
import tkinter as TK

#cores 

cor1 = "#0A0A0A"
cor2 = "#1C1C1C"
cor3 = "#E0E0E0"
cor4 = "#FF5722"
cor5 = "#9E9E9E"
cor6 = "#424242"

janela = Tk()
janela.title("DECISOR")
janela.geometry("235x304")
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
b_4  = Button(Frame_corpo, text="7", width=5, height=2, bg=cor2, font=("Ivy 13 bold"), fg=cor3, command=lambda: print("7"))
b_4.place(x=0, y=52)
b_5 = Button(Frame_corpo, text="8", width=5, height=2, bg=cor2, font=("ivy 13 bold"),fg=cor3, command = lambda: print("8") )
b_5.place(x=59, y=52)
b_6 = Button(Frame_corpo, text="9", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, command=lambda: print("9"))
b_6.place(x=118, y=52)
b_7 = Button(Frame_corpo, text="*", width=5, height=2, bg=cor5, font=("ivy 13 bold"), fg=cor1, command=lambda:print("multiplicação"))
b_7.place(x=177,y=52)
b_8 = Button(Frame_corpo, text="4", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, command=lambda:print("4"))
b_8.place(x=0, y=104)
b_9 = Button(Frame_corpo, text="5", width=5, height=2, bg=cor2, font=("iby 13 bold"), fg=cor3, command=lambda:print("5"))
b_9.place(x=59, y=104)
b_10 = Button(Frame_corpo, text="6", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg= cor3 ,command=lambda:print("6"))
b_10.place(x=118, y=104)
b_11 = Button(Frame_corpo, text="-", width=5, height=2, bg=cor5, font=("ivy 13 bold"), fg=cor1, command=lambda:print("subtração"))
b_11.place(x=177, y=104)
b_12 = Button(Frame_corpo, text="1", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, command=lambda:print("1"))
b_12.place(x=0, y=150)
b_13 = Button(Frame_corpo, text="2", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, command=lambda:print("2"))
b_13.place(x=59, y=150)
b_14 = Button(Frame_corpo, text="3", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, command=lambda:print("3"))
b_14.place(x=118, y=150)
b_15 = Button(Frame_corpo, text="+", width=5, height=2, bg=cor5, font=("ivy 13 bold"), fg=cor1, command=lambda:print("+"))
b_15.place(x=177, y=150)
b_16 = Button(Frame_corpo, text="0", width=11, height=2 , bg=cor2, font=("ivy 13 bold"), fg=cor3, command=lambda:print("0"))
b_16.place(x=0, y=202)
B_17 = Button(Frame_corpo , text=".", width=5,height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, command=lambda:print("."))
B_17.place(x=118, y=202)
B_18 = Button(Frame_corpo,text="=", width=5, height=2, bg= cor4, font=("ivy 13 bold"), fg=cor1, command=lambda:print("=")   )
B_18.place(x=177, y=202)



janela.mainloop()


