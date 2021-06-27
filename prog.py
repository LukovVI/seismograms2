import os
import cv2
import pandas as pd
import openpyxl
import tkinter

def btn_click()
    print("работаю")

root = tkinter.Tk()

root["bg"] = "#fafafa"
root.title("сейсмограммы")
root.wm_attributes("-alpha", 1)
root.geometry("600x500")

root.resizable(width=True, height=True)

canvas = tkinter.Canvas(root, height=400, width=300)
canvas.pack()

frame = tkinter.Frame(root, bg="red")
frame.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)

title = tkinter.Label(frame, text="Дороу", bg="gray", font=40)
title.pack()

btn = tkinter.Button(frame, text="кнопка", bg="blue", command=btn_click)
btn.pack()



root.mainloop()