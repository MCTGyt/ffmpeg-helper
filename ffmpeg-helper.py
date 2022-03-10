#!/usr/bin/python3
 
import os
import tkinter
top = tkinter.Tk()
top.title("ffmpeg助手")
top.geometry('500x300')

def start():
    tkinter.messagebox.showinfo(title='Start', message='开始压缩，自定义选项将在下个版本开放')
    os.system("ffmpeg" +" " + "-i" + " " + e2.get() + " " + "-s" + " " + "vga" + " " + e3.get())

l1 = tkinter.Label(top, text="源文件")
e2 = tkinter.Entry(top, show=None, font=('Arial', 14))  # 显示成明文形式
l2 = tkinter.Label(top, text="输出文件")
e3 = tkinter.Entry(top, show=None, font=('Arial', 14))  # 显示成明文形式
b1 = tkinter.Button(top, text="开始", font=('Arial', 12), width=10, height=1, command=start)
l1.pack()
e2.pack()
l2.pack()
e3.pack()
b1.pack()

# 进入消息循环
top.mainloop()