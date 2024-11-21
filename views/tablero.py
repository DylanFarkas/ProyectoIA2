import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

class Tablero:
    def __init__(self, master):
        self.master = master
        self.master.title("Smart Horses")
        self.master.geometry("400x400")

        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.img_caballoB = Image.open("resources/imgs/caballo_blanco.png")  
        self.img_caballoN = Image.open("resources/imgs/caballo_negro.png") 
        self.img_x2 = Image.open("resources/imgs/x2.png") 

        self.img_caballoB = self.img_caballoB.resize((50, 50), Image.Resampling.LANCZOS)
        self.img_caballoN = self.img_caballoN.resize((50, 50), Image.Resampling.LANCZOS)
        self.img_x2 = self.img_x2.resize((40, 40), Image.Resampling.LANCZOS)

        self.img_caballoB = ImageTk.PhotoImage(self.img_caballoB)
        self.img_caballoN = ImageTk.PhotoImage(self.img_caballoN)
        self.img_x2 = ImageTk.PhotoImage(self.img_x2)

        self.tablero = np.zeros((8, 8), dtype=int)

        self.generar_entorno()

        self.crear_tablero()

    def crear_tablero(self):
        cell_size = 50
        
        for row in range(8):
            for col in range(8):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                valor = self.tablero[row, col]
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="darkgray", width=2)

                if valor == -1:  # Casilla con x2
                    self.canvas.create_image(x1 + cell_size // 2, y1 + cell_size // 2, image=self.img_x2)
                elif valor != 0:  # Casillas con números
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray", outline="darkgray", width=2)
                    self.canvas.create_text(x1 + cell_size // 2, y1 + cell_size // 2, text=str(valor), font=("Arial", 12, "bold"))

        self.canvas.create_image(self.posicion_caballoB[1] * 50 + 25, self.posicion_caballoB[0] * 50 + 25, image=self.img_caballoB)
        self.canvas.create_image(self.posicion_caballoN[1] * 50 + 25, self.posicion_caballoN[0] * 50 + 25, image=self.img_caballoN)

    def generar_entorno(self):
        casillas_ocupadas = set()
        
        # Generar las casillas con símbolos x2 (4 casillas)
        for _ in range(4):
            while True:
                fila, columna = np.random.randint(0, 8), np.random.randint(0, 8)
                if (fila, columna) not in casillas_ocupadas: 
                    self.tablero[fila, columna] = -1 
                    casillas_ocupadas.add((fila, columna))
                    break

        # Generar las posiciones iniciales del Caballo Blanco
        while True:
            fila, columna = np.random.randint(0, 8), np.random.randint(0, 8)
            if (fila, columna) not in casillas_ocupadas:
                self.posicion_caballoB = (fila, columna)
                casillas_ocupadas.add((fila, columna))
                break

        # Generar las posiciones iniciales del Caballo Negro
        while True:
            fila, columna = np.random.randint(0, 8), np.random.randint(0, 8)
            if (fila, columna) not in casillas_ocupadas: 
                self.posicion_caballoN = (fila, columna)
                casillas_ocupadas.add((fila, columna)) 
                break

        puntos = list(range(1, 11))  # Puntos del 1 al 10
        for num in puntos:
            while True:
                fila, columna = np.random.randint(0, 8), np.random.randint(0, 8)
                if (fila, columna) not in casillas_ocupadas: 
                    self.tablero[fila, columna] = num
                    casillas_ocupadas.add((fila, columna))
                    break

        self.img_caballoB_ref = self.img_caballoB
        self.img_caballoN_ref = self.img_caballoN
        self.img_x2_ref = self.img_x2

        print(f"Posicion Caballo B: {self.posicion_caballoB}")
        print(f"Posicion Caballo N: {self.posicion_caballoN}")
        print("Tablero generado:")
        print(self.tablero)

    def obtener_posicion_caballoB(self):
        return self.posicion_caballoB

    def obtener_posicion_caballoN(self):
        return self.posicion_caballoN

    def obtener_tablero(self):
        return self.tablero