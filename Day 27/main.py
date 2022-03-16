from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=20)
#Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100,y=0)
my_label.grid(column=0,row=0)
my_label.config(padx=100,pady=100)

#Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text='Click Me',command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

new_button = Button(text='New Click Me',command=button_clicked)
# button.pack()
new_button.grid(column=3,row=0)

#Entry
input = Entry(width=10)
# input.pack()
input.grid(column=4,row=2)
print(input.get())

window.mainloop()