import tkinter
from tkinter import *



class GUI:
    def __init__(self, title, w=400, h=400):
        self.window = Tk()
        self.window.title(title)
        self.window.minsize(width=w, height=h)
        self.window.grid(heightInc=3,widthInc=3)
        self.addComps()
        self.mainloop()

    def mainloop(self):
        self.window.mainloop()

    def actionLisenter(self):
        cur = label.cget("text")
        global big
        if big == False:
            label.config(text=cur.upper())
            big = not big
        else:
            label.config(text=cur.lower())
            big = not big


    def addComps(self):
        global label, clicker, bigger, big
        big=False
        label = Label(text="size", font=("",40,"bold"))
        label.grid(row=2,column=2)
        clicker = Button(text="T-Adder", command=self.actionLisenter, font=("",30,"bold"),fg="red",bg="black")
        clicker.grid(row=0,column=1)


class Other(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.create()

    def create(self):
        self.quit=Button(self,text="quit",command=self.quit)
        self.quit.grid()

def main():
    try:
        # GUI("random")
        something = Other()
        something.mainloop()
    except KeyboardInterrupt:
        print("exited program")


if __name__ == '__main__':
    main()
