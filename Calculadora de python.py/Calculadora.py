from tkinter import *
import tkinter as TK 

root = Tk()

class Application():
    def __init__(self,root):
        self.root = root
        self.tela()
        root.mainloop()

        
    def tela(self):
        self.root.title("DECISOR")    
        self.root.configure(background= 'black')
        self.root.geometry("700x500")
        self.root.resizable(False , False)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=500 , height=300)

if __name__ == "__main__": 
    app = Application(root) 
    root.mainloop() 
       



