from views.tablero import Tablero

class Principiante:
    def __init__(self, master):
        self.cargar_tablero(master)
    
    def cargar_tablero(self, master):
        self.tablero = Tablero(master)