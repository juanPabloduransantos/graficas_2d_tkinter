from tkinter import *

#--------------------
# Variables globales
#--------------------
BASE = 460
ALTURA = 220

#--------------------
# Ventana principal
#--------------------
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x265")
ventana_principal.config(bg="white")

# ------------------------------
# Frame de graficacion
# ------------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="black", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# ------------------------------
# Lienzo de graficacion
# ------------------------------
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="darkgray")
c.place(x=10,y=10)

# --------------------
# Rectangulos
# --------------------
rectangulo_1= c.create_rectangle(BASE/1.8, ALTURA/2, BASE/1.1, ALTURA/1.2, fill="red")
rectangulo_1= c.create_rectangle(BASE/1.9, ALTURA/1.8, BASE/1.8, ALTURA/1.3, fill="darkred")
rectangulo_1= c.create_rectangle(BASE/2.1, ALTURA/2, BASE/1.9, ALTURA/1.2, fill="darkred")
rectangulo_1= c.create_rectangle(BASE/1.7, ALTURA/2, BASE/1.6, ALTURA/2.5, fill="darkred")
rectangulo_1= c.create_rectangle(BASE/1.76, ALTURA/2.5, BASE/1.55, ALTURA/3, fill="darkred")
rectangulo_1= c.create_rectangle(BASE/1.4, ALTURA/4.6, BASE/1.12, ALTURA/2, fill="red")
rectangulo_1= c.create_rectangle(BASE/1.35, ALTURA/3.7, BASE/1.15, ALTURA/2.2, fill="darkgray")
rectangulo_1= c.create_rectangle(BASE/1.1, ALTURA/7, BASE/1.43, ALTURA/4.7, fill="darkred")
rectangulo_1= c.create_rectangle(BASE/1.12, ALTURA/12, BASE/1.4, ALTURA/7, fill="darkred")

# --------------------
# Circulos
# --------------------
circulo_1 = c.create_oval(BASE/1.1+10, ALTURA, BASE/1.35+30, ALTURA/1.5+20, fill="darkred")
circulo_1 = c.create_oval(BASE/1.35-30, ALTURA, BASE/1.35+30, ALTURA/1.5+20, fill="darkred")
circulo_1 = c.create_oval(BASE/1.5-60, ALTURA, BASE/1.35-30, ALTURA/1.5+20, fill="darkred")
circulo_1 = c.create_oval(BASE/1.25-30, ALTURA/2.9-30, BASE/1.24+30, ALTURA/2.9+30, fill="beige")
circulo_1 = c.create_oval(BASE/1.25-5, ALTURA/2.5-7, BASE/1.24+5, ALTURA/2.5+7, fill="crimson")
circulo_1 = c.create_oval(BASE/1.2-7, ALTURA/3.2-9, BASE/1.19+7, ALTURA/3.2+9, fill="darkgray")
circulo_1 = c.create_oval(BASE/1.31-7, ALTURA/3.2-9, BASE/1.29+7, ALTURA/3.2+9, fill="darkgray")
circulo_1 = c.create_oval(BASE/1.31-3, ALTURA/3.2-5, BASE/1.29+3, ALTURA/3.2+5, fill="brown")
circulo_1 = c.create_oval(BASE/1.2-3, ALTURA/3.2-5, BASE/1.19+3, ALTURA/3.2+5, fill="brown")

# --------------------
# Lineas rectas
# --------------------
linea_1 = c.create_line(BASE/1.25, ALTURA/3.5, BASE/1.2, ALTURA/4.2, fill="yellow", width=7)
linea_1 = c.create_line(BASE/1.3, ALTURA/4, BASE/1.25, ALTURA/3.3, fill="yellow", width=7)

# --------------------
# Rectangulos2
# --------------------

rectangulo_1= c.create_rectangle(BASE/1.18, ALTURA/1.2, BASE/1.3, ALTURA/1.12, fill="red")
rectangulo_1= c.create_rectangle(BASE/1.57, ALTURA/1.2, BASE/1.4, ALTURA/1.12, fill="red")

# --------------------
# Dibujar texto
# --------------------
texto_1 = c.create_text(BASE/1.5, ALTURA/1.6,anchor="center", text="Juan", font=("Arial", 25, "bold"),fill="darkred", activefill="darkred")

#-------------------------------
# Desplegar ventana principal
#-------------------------------

ventana_principal.mainloop()