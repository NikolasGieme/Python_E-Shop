from tkinter import *
window = Tk()
window.geometry('950x630')


class Menu:
    def __init__(self, name, obj1, obj2, obj3, obj4, value1, value2, value3, value4, x, y):
        self.rb1 = IntVar()
        self.rb2 = IntVar()
        self.rb3 = IntVar()
        self.rb4 = IntVar()
        self.name = name
        self.x = x
        self.y = y
        self.obj1 = obj1
        self.obj2 = obj2
        self.obj3 = obj3
        self.obj4 = obj4
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        self.main_label = Label(window, text=self.name, font=5, bg="red", relief=RAISED, borderwidth=7, anchor=N, height=10, width=25)
        self.main_label.place(x=self.x, y=self.y)
        self.checkbutton1 = Checkbutton(window, text=self.obj1+": "+str(self.value1)+"€", bg="yellow", height=5, relief=RAISED, borderwidth=5, width=14, var=self.rb1)
        self.checkbutton1.place(x=self.x+9, y=self.y+40)
        self.checkbutton2 = Checkbutton(window, text=self.obj2+": "+str(self.value2)+"€", bg="yellow", height=5, relief=RAISED, borderwidth=5, width=14, var=self.rb2)
        self.checkbutton2.place(x=self.x+146, y=self.y+40)
        self.checkbutton3 = Checkbutton(window, text=self.obj3+": "+str(self.value3)+"€", bg="yellow", height=5, relief=RAISED, borderwidth=5, width=14, var=self.rb3)
        self.checkbutton3.place(x=self.x+9, y=self.y+140)
        self.checkbutton4 = Checkbutton(window, text=self.obj4+": "+str(self.value4)+"€", bg="yellow", height=5, relief=RAISED, borderwidth=5, width=14, var=self.rb4)
        self.checkbutton4.place(x=self.x+146, y=self.y+140)


fridge = Menu("Refrigerators", "Miele\nKFN15943SD\nED/CS", "Siemens\niQ70\nKG56FSBDA", "Neff\nKG7493BD0", "Bosch\nKGN864IFA", 2500, 1459, 1515, 1770, 10, 70)
ovens = Menu("Ovens", "Siemens\nHB513ABR00", "Bosch\nHBA513BB1", "Miele\nΗ 7460 B", "Neff\nB3AVH4HN1", 529, 599, 1699, 1299, 320, 70)
dishwashers = Menu("Dishwashers", "Siemens\nSN25ZI55CE", "Bosch\nSMS4HDW52E", "Whirlpool\nWFO 3O33 DL\nX 60cm Inox", "Morris\nTTW-55081\nWhite", 1305, 905, 619, 359, 10, 340)
window.mainloop()
