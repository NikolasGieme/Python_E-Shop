from tkinter import *
window = Tk()
root = Tk()
root.title("NickMart")
root.geometry('420x100')
window.title("NickMart")
window.geometry('950x650')
totalvalue = 0


def Check():
    window.destroy()
    Label(root, text="The total value of the stuff you bought is "+str(totalvalue)+"€.\nEverything will arrive at your home in 5 to 10 working days.", font=20, relief=SUNKEN, borderwidth=7, bg="dodgerblue").pack()
    Button(root, text="Done", font=20, relief=RAISED, borderwidth=5, bg="blue", fg="White", command=lambda: root.destroy()).place(x=180, y=55)
    root.mainloop()


class Menu:
    global totalvalue

    def __init__(self, name, obj1, obj2, obj3, obj4, value1, value2, value3, value4, x, y):
        global totalvalue
        self.rb1 = BooleanVar()
        self.rb2 = BooleanVar()
        self.rb3 = BooleanVar()
        self.rb4 = BooleanVar()
        self.rb1.set(False)
        self.rb2.set(False)
        self.rb3.set(False)
        self.rb4.set(False)
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
        self.main_label = Label(window, text=self.name, font=5, bg="blue", fg="white", relief=RAISED, borderwidth=7, anchor=N, height=13, width=31)
        self.main_label.place(x=self.x, y=self.y)
        self.checkbutton1 = Checkbutton(window, text=self.obj1+": "+str(self.value1)+"€", bg="dodgerblue", height=5, relief=RAISED, borderwidth=5, width=14, var=self.rb1)
        self.checkbutton1.place(x=self.x+12, y=self.y+40)
        self.checkbutton2 = Checkbutton(window, text=self.obj2+": "+str(self.value2)+"€", bg="dodgerblue", height=5, relief=RAISED, borderwidth=5, width=14, var=self.rb2)
        self.checkbutton2.place(x=self.x+150, y=self.y+40)
        self.checkbutton3 = Checkbutton(window, text=self.obj3+": "+str(self.value3)+"€", bg="dodgerblue", height=5, relief=RAISED, borderwidth=5, width=14, var=self.rb3)
        self.checkbutton3.place(x=self.x+12, y=self.y+140)
        self.checkbutton4 = Checkbutton(window, text=self.obj4+": "+str(self.value4)+"€", bg="dodgerblue", height=5, relief=RAISED, borderwidth=5, width=14, var=self.rb4)
        self.checkbutton4.place(x=self.x+150, y=self.y+140)
        self.rb1.trace("w", self.FinalCheck)
        self.rb2.trace("w", self.FinalCheck)
        self.rb3.trace("w", self.FinalCheck)
        self.rb4.trace("w", self.FinalCheck)

    def FinalCheck(self, *args):
        global totalvalue
        if self.rb1.get():
            totalvalue += self.value1
        if self.rb2.get():
            totalvalue += self.value2
        if self.rb3.get():
            totalvalue += self.value3
        if self.rb4.get():
            totalvalue += self.value4


Label(window, text="NickMart\nKitchen Appliances", font=20, width=45, relief=SUNKEN, borderwidth=7, bg="dodgerblue").place(x=270, y=0)
fridge = Menu("Refrigerators", "Miele\nKFN15943SD\nED/CS", "Siemens\niQ70\nKG56FSBDA", "Neff\nKG7493BD0", "Bosch\nKGN864IFA", 2500, 1459, 1515, 1770, 10, 70)
ovens = Menu("Ovens", "Siemens\nHB513ABR00", "Bosch\nHBA513BB1", "Miele\nΗ 7460 B", "Neff\nB3AVH4HN1", 529, 599, 1699, 1299, 320, 70)
hobs = Menu("Kitchen Hobs", "Miele\nKM 7684\nFL", "Siemens\nEX875KYW1E", "Neff\nT68TS6RN0", "Franke\nFHR 604 C\nT BK", 1999, 1669, 1559, 545, 630, 70)
dishwashers = Menu("Dishwashers", "Siemens\nSN25ZI55CE", "Bosch\nSMS4HDW52E", "Whirlpool\nWFO 3O33 DL\nX 60cm Inox", "Morris\nTTW-55081\nWhite", 1305, 905, 619, 359, 10, 340)
rangehoods = Menu("Kitchen Range Hoods", "Miele\nDA6698W Puristic\nEdition 6000", "Siemens\nLC97BHM50", "Electrolux\nLFT769X", "Franke\nSmart Deco\nFSMD 508", 2100, 679, 519, 429, 320, 340)
microwaves = Menu("Microwaves", "Bosch\nBFL634GB1", "Miele\nM 2230\nSC BK", "Neff\nHLAWD23N0", "Siemens\nBE550LMR0", 729, 849, 579, 559, 630, 340)
buy = Button(window, text="Order", font=10, width=25, relief=SUNKEN, borderwidth=7, bg="dodgerblue", command=Check)
buy.place(x=350, y=600)

window.mainloop()
