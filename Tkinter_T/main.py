from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

top = Tk()
top.geometry("450x300")
"""
Button1 =  Button(top,text="Submit").place(x=0 ,y=0)
Button2 =  Button(top,text="Submit").place(x=50,y=0)
Button3 = Button(top,text="Submit").place(x=0 ,y=30)
Button4 = Button(top,text="Submit").place(x=50  ,y=30)
"""
###EXERCICE 3
"""
    Button1 =  Button(top,width=20,height=2,text="Button1").place(x=10 ,y=10)
Button2 =  Button(top,width=20,height=2,text="button2").place(x=200 ,y=10)
Button3 =  Button(top,width=20,height=2,text="Button3").place(x=10 ,y=100)
Button4 =  Button(top,width=20,height=2,text="Button4").place(x=200 ,y=100)
"""

#Exercice 4

"""
def action():
    name = entryName.get()
    v.set("Hello " + name)



# création du label qui affiche le résultat
v = StringVar()
lblResult = Label(top, textvariable=v).place(x=100, y=50)


# création du champ de saisie Entry
entryName = Entry(top).place(x=100, y=80, width=150)

# création du bouton valider
btn_validate = Button(top, text="Validate!", command=action).place(x=100, y=110, width=150)

top.mainloop()
"""
x=np.linspace(-5,5,100)
plt.plot(x,np.sin(x))  # on utilise la fonction sinus de Numpy



canvas = FigureCanvasTkAgg(plt.show(), master=top)  # A tk.DrawingArea.
canvas.draw()


