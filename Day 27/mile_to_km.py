from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#Button
def button_clicked():
    new_text = input.get()
    my_label4.config(text=round(int(new_text)*1.609344,2))

input = Entry(width=10)
# input.pack()
input.grid(column=1,row=0)
print(input.get())

my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.grid(column=2,row=0)
# my_label.config(padx=100,pady=100)

my_label2 = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label2.grid(column=0,row=1)
# my_label.config(padx=100,pady=100)

my_label3 = Label(text="Km", font=("Arial", 24, "bold"))
my_label3.grid(column=2,row=1)
# my_label.config(padx=100,pady=100)

my_label4 = Label(text="0", font=("Arial", 24, "bold"))
my_label4.grid(column=1,row=1)
# my_label.config(padx=100,pady=100)

button = Button(text='Calculate',command=button_clicked)
# button.pack()
button.grid(column=1,row=2)


window.mainloop()