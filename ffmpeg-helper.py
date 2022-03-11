#!/usr/bin/python3
 
import webbrowser
import os
import tkinter
top = tkinter.Tk()
top.title("ffmpeg助手")
top.geometry('500x300')

def start():
    if e2.get() != "" :
        if e4.get() != "" :
            if e3.get() != "" :
                os.system("ffmpeg" +" " + "-i" + " " + e2.get() + " " + e4.get() + " " + e3.get())
            else :
                print("你未输入资料")
        else :
            print("你未输入资料")
    else :
        print("你未输入资料")
    #tkinter.messagebox.showinfo(title='Start', message='开始压缩，自定义选项将在下个版本开放')


def open_blog(event):
    webbrowser.open_new_tab("https://mctg.ink")

l1 = tkinter.Label(top, text="源文件*")
e2 = tkinter.Entry(top, show=None, font=('Arial', 14))  # 显示成明文形式
l2 = tkinter.Label(top, text="输出文件*")
e3 = tkinter.Entry(top, show=None, font=('Arial', 14))  # 显示成明文形式
b1 = tkinter.Button(top, text="开始", font=('Arial', 12), width=10, height=1, command=start)
e4 = tkinter.Entry(top, text="-s vga")
l5 = tkinter.Label(top, text="自定义参数 例如 -s vga*")

l4 = tkinter.Label(top, text="by 天哥de博客", fg="blue")
l4.bind("<Button-1>", open_blog)

l1.pack() #源文件
e2.pack() #源文件input
l2.pack() #输出文件
e3.pack() #输出文件input
l5.pack() #自定义参数
e4.pack() #自定义参数input
b1.pack() #开始button
l4.pack() #blog_link


# 进入消息循环
top.mainloop()