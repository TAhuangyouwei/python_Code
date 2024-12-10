from tkinter import *  # 导入 tkinter 的控件类和常用功能
from tkinter import messagebox  # 导入消息框
from tkinter import filedialog  # 导入文件对话框

root = Tk()
root.title("我的第一个GUI程序")
root.geometry("300x100+1024+512")

def open_file():
    file = filedialog.askopenfilename()  # 打开文件对话框
    if file:
        print(f"打开的文件是: {file}")

def show_message():
    messagebox.showinfo("Info", "这是一个消息框")  # 弹出消息框

Button(root, text="打开文件", command=open_file).pack()
Button(root, text="显示消息", command=show_message).pack()

root.mainloop()

