#Data Access Object
""" Almacenar datos de un estudiante """
"""Create
   Read
   Update
   Delete"""
class StudentDao: 
    def __init__(self):
        self.datos = []

    def add(self, dato):
        self.datos.append(dato)

    def show(self):
        for dato in self.datos:
            print(dato)

    def __str__(self):
        return self.datos