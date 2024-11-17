import tkinter as tk
import customtkinter
from views.ventana_dificultad import Ventana_Dificultad

customtkinter.set_appearance_mode("Dark")

class Ventana_Inicial(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Horses")
        self.geometry("370x250")
        self.resizable(False, False)
        
        # Centrar la ventana 
        self.update_idletasks()  # Actualiza el tamaño de la ventana
        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")
        
        self.iniciar_componentes()
    
    def abrir_ventana(self):
        Ventana_Dificultad()
    
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
        self.LTitulo.place(x=190, y=40, anchor=tk.CENTER)

        #Boton de iniciar
        self.BIniciar = customtkinter.CTkButton(
            master=self,
            width=120,
            height=25,
            corner_radius=10,
            text="Jugar",
            font=("", 30, "bold"),
            fg_color=("#1F6CA7"),
            bg_color=("#242424"),
            hover_color="lightblue",
            cursor="heart",
            command=self.abrir_ventana
            )
        self.BIniciar.place(x=125, y=130)