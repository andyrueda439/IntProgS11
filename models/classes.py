class Student:
    def __init__(self, names, lastnames, career, year, average):
            self.names = names
            self.lastnames = lastnames
            self.career = career
            self.year = year
            self.average = average


    def __str__(self):
          return f"Nombre: {self.names} \nApellidos : {self.lastnames} \nCarrera: {self.career} \nAño : {self.year} \nPromedio {self.average}"