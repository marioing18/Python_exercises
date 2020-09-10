import tkinter as tk
import tkinter.messagebox as msgbox

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        self.label_text = tk.StringVar()
        self.label_text.set("Me llamo:")

        self.name_text = tk.StringVar()

        self.label = tk.Label(self, textvariable = self.label_text)
        self.label.pack(fill = tk.BOTH, expand = 1, padx = 100, pady = 50)

        self.name_entry = tk.Entry(self, textvar = self.name_text)
        self.name_entry.pack(fill = tk.BOTH, expand = 1, padx = 20, pady = 20)

        boton_hola = tk.Button(self, text = "Dí hola",
                                command = self.saluda)
        boton_hola.pack(side = tk.LEFT, padx = (20, 0), pady =(0, 20))

        boton_adios = tk.Button(self, text = "Adios",
                                command = self.adios)
        boton_adios.pack(side = tk.RIGHT, padx = (0,20), pady = (0, 20))

    
    def saluda(self):
        mensaje = "Hola amigo " + self.name_entry.get()
        msgbox.showwarning("Hola!!", mensaje)
    
    def adios(self):
        if msgbox.askyesno("Cierra ventanita", "¿Va a cerrar la ventanita?"):
            
            mensaje = "La ventana cerrará en 2 seg. Hasta luego " + self.name_text.get()
            self.label_text.set(mensaje)
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo("No cerrado", "Sí. ¡¡Seguimos abiertos!!")
        

if __name__ == "__main__":
    ventanita = Ventana()
    ventanita.mainloop()