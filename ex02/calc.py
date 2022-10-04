import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.geometry("300x500")

#左クリックしたら
def button_click(event):
    btn = event.widget
    n= btn["text"]
    event.widget["bg"] = "red"
    #tkm.showinfo(f"{n}",f"{n}ボタンがクリックされました")
    entry.insert(tk.END,n)

#右クリックしたら
def right_click(event):
    entry.delete(0,tk.END)
    event.widget["bg"] = "white"

def click_equal(event):
    a = entry.get()
    result = eval(a)
    entry.delete(0,tk.END)
    entry.insert(tk.END,result)

entry = tk.Entry(root,width=10,font=("",40),justify="right",bg="gray")
entry.grid(row=0,column=0,columnspan=3)


r,c=1,0
suji = list(range(9,-1,-1))
enzanshi = ["+"]
for i,n in enumerate(suji+enzanshi,1):
    btn = tk.Button(root,text=f"{n}",font=("",30),width=4,height=2)
    btn.bind("<1>",button_click)
    btn.bind("<3>",right_click)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 == 0:
        r+= 1
        c =0
    

btn = tk.Button(root,text="=",font=("",30),width=4,height=2)
btn.bind("<1>",click_equal)
btn.grid(row=r,column=c)
root.mainloop()