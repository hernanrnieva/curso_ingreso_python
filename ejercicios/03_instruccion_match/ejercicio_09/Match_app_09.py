import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Hernan
Apellido: Nieva
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
    
    def btn_informar_on_click(self):
        estacion, destino = self.combobox_estaciones.get(), self.combobox_destino.get()
        AUMENTO_20, AUMENTO_10, DESCUENTO_20, DESCUENTO_10, ESTADIA = 1.2, 1.1, 0.8, 0.9, 15000
        multiplicador = 1

        match estacion:
            case "Invierno":
                match destino:
                    case "Bariloche":
                        multiplicador = AUMENTO_20
                    case "Mar del plata":
                        multiplicador = DESCUENTO_20
                    case _:
                        multiplicador = DESCUENTO_10
            case "Verano":
                match destino:
                    case "Bariloche":
                        multiplicador = DESCUENTO_20
                    case "Mar del plata":
                        multiplicador = AUMENTO_20
                    case _:
                        multiplicador = AUMENTO_10
            case _:
                match destino:
                    case "Bariloche" | "Cataratas" | "Mar del plata":
                        multiplicador = AUMENTO_10

        alert("Esto es una alerta", "El precio final es " + str(multiplicador * ESTADIA))
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()