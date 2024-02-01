import tkinter as tk
from GeradorDeFicha import Atributos_auto
import customtkinter

def on_button_click():
    Atributos_auto()
#primeiro uso da biblioteca tkinter !
root = tk.Tk()
#cria um botão
CRIAR = tk.Button( text="gerar ficha", command= on_button_click)
CRIAR.pack()
#deixa a janela aberta
root.mainloop()