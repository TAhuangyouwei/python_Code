from tkinter import *
from tkinter import messagebox  # 导入消息框模块


class Application(Frame):
    """一个基本的GUI程序示例，使用面向对象的方式"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建按钮并设置文字
        self.btn01 = Button(self, text="点击发送")
        self.btn01.pack()
        # 设置按钮的命令为 songhua 方法，当按钮点击时调用
        self.btn01["command"] = self.songhua

        # 创建一个退出按钮
        self.btnExit = Button( text="退出", command=self.master.destroy)
        self.btnExit.pack()

    def songhua(self):
        # 显示信息框
        messagebox.showinfo("提示", "送你99朵玫瑰花")

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个基础GUI程序案例")
    app = Application(master=root)
    root.mainloop()
