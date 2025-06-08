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

#variavel Todos valores
todos_valores = ''


#criaçaõ do label
valor_texto = StringVar()


#criação da função
def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)



    #passando o valor para ir na tela
    valor_texto.set(todos_valores)


  # funçao para calcular 

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    


#função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


#label
app_label = Label(Frame_tela, textvariable= valor_texto, width=16, height=2, padx=7, relief=FLAT, font='ivy 18', anchor="e", justify=RIGHT, bg=cor3)
app_label.place(x=0, y=0)






#criando os botões

b_1= Button(Frame_corpo,text="C",width= 11, height=2, bg=cor4, font=("Ivy 13 bold"), fg=cor1, command=limpar_tela)
b_1.place(x=0, y=0)
b_2= Button(Frame_corpo, command= lambda : entrar_valores('%') ,text="%",width= 5, height=2 ,bg= cor5, font=("Ivy 13 bold"), fg=cor1, )
b_2.place(x=118, y=0)
b_3 = Button(Frame_corpo, command = lambda : entrar_valores('/') , text="/", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), fg=cor1)    
b_3.place(x=177, y=0)
b_4  = Button(Frame_corpo,command = lambda : entrar_valores('7') ,
 text="7", width=5, height=2, bg=cor2, font=("Ivy 13 bold"), fg=cor3, )
b_4.place(x=0, y=52)
b_5 = Button(Frame_corpo,command = lambda : entrar_valores('8') ,text="8", width=5, height=2, bg=cor2, font=("ivy 13 bold"),fg=cor3  )
b_5.place(x=59, y=52)
b_6 = Button(Frame_corpo,command = lambda : entrar_valores('9') , text="9", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3 )
b_6.place(x=118, y=52)
b_7 = Button(Frame_corpo,command= lambda : entrar_valores('*') ,text="*", width=5, height=2, bg=cor5, font=("ivy 13 bold"), fg=cor1)
b_7.place(x=177,y=52)
b_8 = Button(Frame_corpo,command= lambda : entrar_valores('4') ,text="4", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, )
b_8.place(x=0, y=104)
b_9 = Button(Frame_corpo,command= lambda : entrar_valores('5') ,text="5", width=5, height=2, bg=cor2, font=("iby 13 bold"), fg=cor3, )
b_9.place(x=59, y=104)
b_10 = Button(Frame_corpo,command= lambda : entrar_valores('6') , text="6", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg= cor3 ,)
b_10.place(x=118, y=104)
b_11 = Button(Frame_corpo,command= lambda : entrar_valores('-') ,text="-", width=5, height=2, bg=cor5, font=("ivy 13 bold"), fg=cor1, )
b_11.place(x=177, y=104)
b_12 = Button(Frame_corpo,command= lambda : entrar_valores('1') , text="1", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, )
b_12.place(x=0, y=150)
b_13 = Button(Frame_corpo,command= lambda : entrar_valores('2'), text="2", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, )
b_13.place(x=59, y=150)
b_14 = Button(Frame_corpo,command= lambda : entrar_valores('3') ,text="3", width=5, height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, )
b_14.place(x=118, y=150)
b_15 = Button(Frame_corpo,command= lambda : entrar_valores('+'), text="+", width=5, height=2, bg=cor5, font=("ivy 13 bold"), fg=cor1, )
b_15.place(x=177, y=150)
b_16 = Button(Frame_corpo, text="0", width=11, height=2 , bg=cor2, font=("ivy 13 bold"), fg=cor3, command=lambda:print("0"))
b_16.place(x=0, y=202)
B_17 = Button(Frame_corpo ,command= lambda : entrar_valores('.'), text=".", width=5,height=2, bg=cor2, font=("ivy 13 bold"), fg=cor3, )
B_17.place(x=118, y=202)
B_18 = Button(Frame_corpo,command= calcular,
text="=", width=5, height=2, bg= cor4, font=("ivy 13 bold"), fg=cor1,    )
B_18.place(x=177, y=202)




janela.mainloop()


