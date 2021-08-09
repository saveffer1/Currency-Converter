from tkinter import *
from tkinter.ttk import Combobox
from google_currency import convert
import json
from tkinter import messagebox

root = Tk()
root.geometry("600x400")
root.title("Currency Convertor")
root.iconbitmap("tcddr.ico")
root.config(bg="gray40")

with open("Currency Code.txt") as f:
    lines = f.readlines()

dictop = {}    
for line in lines:
    opaq = line.split("\t");
    dictop[opaq[1]] =  opaq[2]

def functionbutton():
    try:
        lightbox = Combobox1.get()
        heavybox = Combobox2.get()
        lapto = dictop[lightbox]
        lapti = dictop[heavybox]
        serial = var1.get() 
        opol = convert(lapto, lapti, serial)
        lope = json.loads(opol)
        jsonfix = lope["amount"]
        var2.set(jsonfix)
    except:
        rr = messagebox.askretrycancel("A Problem Has Been Occured", "Please Check your Internet Connection or Check the Amount You Have Entered.")

Title = Label(root, text="Currency Convertor", fg="White",  bg="gray40", font=("ubuntu", 15, "italic"))
Title.place(x=200, y=10)

Lable1 = Label(root, text="Amount to Convert :- ", bg="gray40",
               fg="white", font=("ubuntu", 15, "bold"))
Lable1.place(x=15, y=60)

var1 = IntVar()
feeder = Entry(root, width=27, text=var1, bg="White",
               fg="blue", font=("ubuntu", 15, "bold"))
feeder.place(x=280, y=60)

Label2 = Label(root, text="Convert From :- ", bg="gray40",
               fg="white", font=("ubuntu", 10, "bold"))
Label2.place(x=15, y=120)

slider = StringVar()
Combobox1 = Combobox(root, width=30, textvariable=slider, state="readonly", font=("ubuntu", 10, "bold"))
Combobox1['values'] = [item for item in dictop.keys()]
Combobox1.current(1)
Combobox1.place(x=320, y=120)

Lable3 = Label(root, text="Convert To :-  ", bg="gray40",
               fg="white", font=("ubuntu", 10, "bold"))
Lable3.place(x=15, y=160)

foreground = StringVar()
Combobox2 = Combobox(root, width=30, textvariable=foreground, state="readonly", font=("ubuntu", 10, "bold"))
Combobox2['values'] = [item for item in dictop.keys()]
Combobox2.current(0)
Combobox2.place(x=320, y=160)

Button1 = Button(root, bg="green", text="Convert", command=functionbutton , fg="white", font=("ubuntu", 15, "bold"), relief=RAISED,\
                            cursor="hand2")
Button1.place(x=240, y=220)

Label4 = Label(root, text="Converted Amount :- ",
               bg="gray40", fg="white", font=("ubuntu", 15, "bold"))
Label4.place(x=15, y=280)

var2 = IntVar()
Entry2 = Entry(root, textvariable=var2, fg="blue", state="readonly",width=27, font=("ubuntu", 15, "bold"))
Entry2.place(x=280, y=280)

footer = Label(root, text="This program use google-currency",bg="lightblue", fg="grey", font=("ubuntu", 15, "bold"))
footer.place(x=130, y=340)

footer = Label(root, text="Developed By โชติวัฒน์ บุญพ่วง",
               bg="lightblue", fg="grey", font=("ubuntu", 15, "bold"))
footer.place(x=160, y=370)

root.mainloop()
