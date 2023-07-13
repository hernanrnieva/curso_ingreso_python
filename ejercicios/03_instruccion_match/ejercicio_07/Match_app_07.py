import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Hernan
Apellido: Nieva
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el 
botón ‘Informar’ indicar el punto cardinal de nuestro país donde se encuentra: 
Norte, Sur, Este u Oeste
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
    
    def btn_informar_on_click(self):
        destino, punto_cardinal = self.combobox_destino.get(), ""

        match destino:
            case "Mar del plata":
                punto_cardinal += "Este"
            case "Cataratas":
                punto_cardinal += "Norte"
            case _:
                punto_cardinal += "Sur"

        if(punto_cardinal):
            alert("Esto es una alerta", "Usted está en " + punto_cardinal)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()