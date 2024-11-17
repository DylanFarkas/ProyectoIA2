from views.ventana_inicial import Ventana_Inicial


class SmartHorses():
    def main(self):
        app = Ventana_Inicial()
        app.mainloop()
        
if __name__ == "__main__":
    SmartHorses().main()