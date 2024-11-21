import tkinter as tk
import customtkinter
from dificultades.principiante import Principiante
from dificultades.amateur import Amateur
from dificultades.experto import Experto

class Ventana_Dificultad(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Smart Horses")
        self.geometry("400x430")
        self.resizable(False, False)
        
        # Centrar la ventana 
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")
        
        self.grab_set()
        self.focus_get()
        self.iniciar_componentes()
        
    def iniciar_componentes(self):
        #Titulo
        self.LTitulo = customtkinter.CTkLabel(
            master=self,
            text="Smart Horses",
            width=230,
            font=("", 25, "bold"),
            text_color="white",
            height=40,
            fg_color=("#1F6CA7"),
            bg_color=("#242424"),
            corner_radius=15
        )
        self.LTitulo.place(x=200, y=40, anchor=tk.CENTER)
        
        
        self.LSeleccionar = customtkinter.CTkLabel(
            master=self, 
            text="Seleccione alguna dificultad",
            width=100,
            height=20,
            font=("", 17),
            text_color="white",
            bg_color=("#242424"),
            corner_radius=8
            )
        self.LSeleccionar.place(x=195, y=120, anchor=tk.CENTER)
        
        self.BPrincipiante = customtkinter.CTkButton(
            master=self,
            width=220,
            height=25,
            corner_radius=10,
            text="Principiante",
            font=("", 20, "bold"),
            fg_color="#242424",
            border_color="#701ef7",
            border_width=2,
            hover_color="#701ef7",
            command=self.iniciar_dificultad_principiante
            
            )
        self.BPrincipiante.place(x=195 ,y=190, anchor=tk.CENTER)
        
        self.BAmateur = customtkinter.CTkButton(
            master=self,
            width=220,
            height=25,
            corner_radius=10,
            text="Amateur",
            font=("", 20, "bold"),
            fg_color="#242424",
            border_color="#3fdee6",
            border_width=2,
            hover_color="#3fdee6",
            command=self.iniciar_dificultad_amateur
            
            )
        self.BAmateur.place(x=195 ,y=250, anchor=tk.CENTER)
        
        self.BExperto = customtkinter.CTkButton(
            master=self,
            width=220,
            height=25,
            corner_radius=10,
            text="Experto",
            font=("", 20, "bold"),
            fg_color="#242424",
            border_color="#249543",
            border_width=2,
            hover_color="#249543",
            command=self.iniciar_dificultad_experto
            
            )
        self.BExperto.place(x=195 ,y=310, anchor=tk.CENTER)
        
        
    def iniciar_dificultad_principiante(self):
        self.juego = Principiante(self)
        print("Se esta jugando en principiante")
    
    def iniciar_dificultad_amateur(self):
        self.juego = Amateur(self)
        print("Se esta jugando en Amateur")
    
    def iniciar_dificultad_experto(self):
        self.juego = Experto(self)
        print("Se esta jugando en Experto")
    
    