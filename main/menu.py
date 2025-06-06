import models.classes as c
import dao.functions as f

datos = f.StudentDao()



def menu():
    print("""
        1. Agregar
        2. Mostrar
        6. Salir
        Digite una opcion:
        """)

def main():
   
    while(True):
        menu()
        option = input()
        if option == '1':
            nombres = input("Nombres del estudiante: ")
            apellidos = input("Apellidos del estudiante: ")
            carrera= input("Carrera: ")
            año = input("Año: ")
            promedio = float(input("Promedio: "))
            dato = c.Student(nombres, apellidos, carrera, año, promedio)
            datos.add(dato)
            
        elif option == '2':
            print("Datos")
            datos.show()
        elif option == '6':
            print("Gracias por compartir tus datos")
            False
            break
        else:
            print("Opcion invalida")