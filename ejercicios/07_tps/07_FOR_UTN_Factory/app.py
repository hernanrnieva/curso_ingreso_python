'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre, edad, genero, tecnologia, senior = "", 0, "", "", ""

        nbs, nombre_jr_menor, edad_jr_menor = 0, "", 0
        cantidad_nbs, edades_nbs, cantidad_fs, edades_fs, cantidad_ms, edades_ms, postulantes = 0, 0, 0, 0, 0, 0, 0
        cantidad_python, cantidad_js, cantidad_asp = 0, 0, 0

        for i in range(0, 10, 1):
            nombre = prompt("Nombre", "Por favor ingrese su nombre")
            edad = int(prompt("Edad", "Por favor ingrese su edad"))
            genero = prompt("Genero", "Por favor ingrese su genero")
            tecnologia = prompt("Tecnologia", "Por favor ingrese su tecnologia")
            senior = prompt("Seniority", "Por favor ingrese su seniority")

            # Generales
            postulantes += 1

            if genero == "NB":
                cantidad_nbs += 1
                edades_nbs += edad
            elif genero == "F":
                cantidad_fs += 1
                edades_fs += edad
            elif genero == "M":
                cantidad_ms += 1
                edades_ms += edad

            if tecnologia == "PYTHON":
                cantidad_python += 1
            elif tecnologia == "JS":
                cantidad_js += 1
            elif tecnologia == "ASP.NET":
                cantidad_asp += 1

            # Específicos
            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and edad > 24 and edad < 41 and senior == "Ssr":
                nbs += 1

            if senior == "Jr":
                if nombre_jr_menor == "":
                    nombre_jr_menor = nombre
                    edad_jr_menor = edad
                elif edad_jr_menor > edad:
                    nombre_jr_menor = nombre
                    edad_jr_menor = edad

        promedio_nbs = 0
        porcentaje_nbs = 0
        if cantidad_nbs != 0:
            promedio_nbs = edades_nbs/cantidad_nbs
            porcentaje_nbs = cantidad_nbs/postulantes*100

        promedio_fs = 0
        porcentaje_fs = 0
        if cantidad_fs != 0:
            promedio_fs = edades_fs/cantidad_fs
            porcentaje_fs = cantidad_fs/postulantes*100

        promedio_ms = 0
        porcentaje_ms = 0
        if cantidad_ms != 0:
            promedio_ms = edades_ms/cantidad_ms
            porcentaje_ms = cantidad_ms/postulantes*100

        tecnologia_mas_postulada = "PYTHON"
        if cantidad_js > cantidad_python:
            if cantidad_js > cantidad_asp:
                tecnologia_mas_postulada = "ASP.NET"
            else:
                tecnologia_mas_postulada = "JS"

        print("Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS "\
              "cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: " + str(nbs))
        print("Nombre del postulante Jr con menor edad: " + nombre_jr_menor)
        print("Promedio de edades por género:\n\tNBs: " + str(promedio_nbs) + "\n\tFs: " + str(promedio_fs) + \
              "\n\tMs: " + str(promedio_ms))
        print("Tecnología con más postulantes: " + tecnologia_mas_postulada)
        print("Porcentaje de postulantes de cada género:\n\tNBs: " + str(porcentaje_nbs) + \
              "\n\tFs: " + str(porcentaje_fs) + "\n\tMs: " + str(porcentaje_ms))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
