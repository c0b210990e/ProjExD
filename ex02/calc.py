import tkinter as tk

root = tk.Tk()
root.geometry("300x500")

r,c=0,0
for i,n in enumerate(range(9,-1,-1),1):
    btn = tk.Button(root,text=f"{n}",font=("Times New Roman",30),width=4,height=2)
    btn.grid(row=r,column=c)
    c += 1
    if i%3 == 0:
        r+= 1
        c =0


root.mainloop()