import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Hernan
Apellido: Nieva
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        numero = int(prompt("Esto es un prompt", "Por favor ingrese un numero"))
        es_primo = True

        for i in range(2, numero // 2 + 1, 1):
            if(numero%i == 0):
                es_primo = False

        mensaje = "El número ingresado "
        if es_primo:
            mensaje += "es primo"
        if not es_primo:
            mensaje += "no es primo"
            
        alert("Esto es una alert", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()