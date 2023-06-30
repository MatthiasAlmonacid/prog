###Actividad N°2 intro prog###

import os
from datetime import datetime

#Objeto de propietario
class Prop:
    def __init__(self, rut, name, age):
        self.rut = rut
        self.name = name
        self.age = age
        self.ing_dt = datetime.now().strftime("%Y%m%d")
        self.ppus = []

    def print_info(self):
        print(f"RUT: {self.rut}\nIngreso: {self.ing_dt}\nNombre: {self.name}\nEdad: {self.age}\nPatente(s): {[i for i in self.ppus]}\n")

    def add_ppu(self, element):
        self.ppus.append(element)

    def get_ppus(self):
        return self.ppus

    #¿declarar setters y getters?

def make_data():
    """
    Se ingresan 2 registros para testear el programa
    Se podrian validar los campos, pero no lo veo necesario
    """
    p1 = ["1-9", "Santiago Castillo", 26]
    p2 = ["1-0", "Sofia Carrasco", 42]

    p1 = Prop(p1[0], p1[1], p1[2])
    p2 = Prop(p2[0], p2[1], p2[2])

    ppus = ["STHR25", "JUFT58", "KI3210"]

    p1.add_ppu(ppus[0])
    p1.add_ppu(ppus[1])
    p2.add_ppu(ppus[2])

    return [p1, p2]

def buscar_prop(rut, props):
    find = 0
    for i in props:
        if i.rut == rut:
            print("Datos encontrados:\n")
            i.print_info()
            find = 1
    if find == 0 and rut != "s":
        print("No se han encontrado datos asociados al rut ingresado.\n")
    return find

def get_prop():
    props = make_data()
    return props


def main():
    props = get_prop()
    print("Bienvenido al sistema de consultas de información sobre propietarios de autos.")

    print("Los ruts disponibles a consultar son:\n")
    for i in props:
        print(f"{i.rut}")

    while True:
        rut = input("\nFavor ingrese el rut a consultar.\nIngrese 's' para salir.\n")
        resp = buscar_prop(rut, props)

        if rut=="s":
            break;

    if resp == 0 and rut != "s":
        print("No se encontraron propietarios asignados al rut ingresado.")

    elif rut == "s":
        print("Ha decidido salir del programa.")

    os.system("pause")

if __name__ == "__main__":
    main()

