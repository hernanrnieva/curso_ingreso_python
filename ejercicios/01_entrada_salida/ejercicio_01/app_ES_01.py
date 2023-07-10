from tkinter.messagebox import showinfo as alert
import customtkinter

'''
nombre: Hernan
apellido: Nieva
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        titulo_alerta, mensaje_alerta = "Esto es una alerta", "Esto no anda, funciona"
        alert(titulo_alerta, mensaje_alerta)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()