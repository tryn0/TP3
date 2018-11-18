from tkinter import *
from tkinter import simpledialog
import feedparser

raiz=Tk()

miFrame=Frame(raiz, width=300, height=400)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=3, pady=5)
cuadroNombre.config(fg="white", show="+")

juego = nombreLabel=Label(miFrame, text="Haz click en Aceptar para conocer las noticias:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=2, pady=5)

def codigoBoton():
    
    juego = simpledialog.askstring("Contesta", "Escribe una palabra clave relacionada con videojuegos para conocer las noticias recientes")
    juego=juego.lower()

    TresDJ = "https://www.3djuegos.com/universo/rss/rss.php"

    noticias3dj = feedparser.parse(TresDJ)['entries']

    for n in noticias3dj:
        if juego in n.title.lower():
            miFrame=Frame(raiz, width=(len(n.title)*30), height=30)
            miFrame.pack()
            Label(miFrame, text=n.title, fg="red", font="0").place(x=0, y=0)

botonAcept=Button(raiz, text="Aceptar", command=codigoBoton)
botonAcept.pack()




raiz.mainloop()

