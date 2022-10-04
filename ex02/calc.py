import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    n= btn["text"]
    tkm.showinfo(f"{n}",f"{n}ボタンがクリックされました")
    entry.insert(tk.END,n)

def click_equal(event):
    a = entry.get()
    result = eval(a)
    entry.delete(0,tk.END)
    entry.insert(tk.END,result)

entry = tk.Entry(root,width=10,font=("",40),justify="right")
entry.grid(row=0,column=0,columnspan=3)

r,c=1,0
suji = list(range(9,-1,-1))
enzanshi = ["+"]
for i,n in enumerate(suji+enzanshi,1):
    btn = tk.Button(root,text=f"{n}",font=("Times New Roman",30),width=4,height=2)
    btn.bind("<1>",button_click)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 == 0:
        r+= 1
        c =0

btn = tk.Button(root,text="=",font=("",30),width=4,height=2)
btn.bind("<1>",click_equal)
btn.grid(row=r,column=c)
root.mainloop()