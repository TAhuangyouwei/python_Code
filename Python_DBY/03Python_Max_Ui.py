from  tkinter import *
from  tkinter import messagebox
root = Tk()
btn01 = Button(root)
btn01["text"] = "点我就送花"
btn01.pack()
def songhua(e):   #e就是事件的对象
    messagebox.showinfo("message", "送你99朵玫瑰花")
    print("送你99朵玫瑰花")
btn01.bind("<Button-1>", songhua)
root.mainloop()