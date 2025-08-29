from tkinter import*

def click():
    print("hi")
window = Tk()
window.geometry("420x420")
window.title("gui program")
window.config(background="white")
label = Label(window,text="hi")
label.pack()
##label.place(x=0,y=0)
button = Button(window,text="click")
button.config(command=click)
button.pack()
window.mainloop()