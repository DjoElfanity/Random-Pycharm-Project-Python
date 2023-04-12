
from tkinter import *

"""
top = Tk()

top.geometry('450x300')
user_name= Label(top ,text="Username").place(x= 40 , y=60)
user_password = Label(top ,text ="Password").place(x =40 , y=100 )
submit_button = Button(top,text="Submit").place(x=40 ,y=130)
user_name_input = Entry(top , width=30 ).place(x=110 , y =60)
user_passwod_input = Entry(top, width=30).place(x=110, y = 100)
"""

class Application(Frame):
    def disconect(self):
        self.sock.close()

    def __init__(self, master ="None"):
        Frame.__init__(self, master)
        self.pack()
        self.createWidget()

    def on(self):
        self.sock.send("o")

    def off(self):
        self.sock.send('f')

    def createWidget(self):
        self.QUIT = Button(self ,height=20,width=20,command=self.quit,text="Quit").pack({'side':'left'})
        self.disconect= Button(self,height=20, width=20 , command=self.disconect,text="Disconect").pack({'side':'left'})
        self.On = Button(self, height=20,width=20 , command=self.on,text="on").pack({'side':'left'})
        self.off = Button(self , height=20 , width=20 , command=self.off , text='off').pack({'side':'left'})




root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()