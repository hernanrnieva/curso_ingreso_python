import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Hernan
Apellido: Nieva
Al presionar el botón 'CARGAR' se le solicitarán tres números al usuario mediante el Dialog Prompt, los mismos deberán ser almacenados en un vector lista_datos. 
Al presionar el botón 'MOSTRAR', se deberán mostrar los números almacenados en el vector utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = []

    def btn_mostrar_on_click(self):
        for i in self.lista_datos:
            alert("Esto es un alert", str(i))
        
    def btn_cargar_on_click(self):
        for i in range(0, 3, 1):
            numero = prompt("Esto es un prompt", "Por favor ingrese un número")

            while numero == None or not numero.isdigit() or numero == "" :
                numero = prompt("Esto es un prompt", "Por favor ingrese un número válido")

            self.lista_datos.append(int(numero))
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()