class Personas:
    def __init__(self, nombre: str = "pepe", apellido: str = "cavani", dni: int = 45715028):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni 

    def mostrar_personas(self):
        print(f"mis datos son = {self.__nombre__} 
              apellido = {self.__apellido__}   
              documento = {self.__dni__}")