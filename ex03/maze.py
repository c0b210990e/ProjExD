import tkinter as tk

def key_down(event): #練習5
    global key
    key = event.keysym


def key_up(event): #練習6
    global key
    key = ""



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1
    canv = tk.Canvas(root,width = 1500, height = 900, bg = "black") #練習2
    canv.pack()
    tori = tk.PhotoImage(file="fig/6.png") #練習3
    cx, cy = 300, 400
    canv.create_image(cx, cy, image = tori, tag="tori")

    #練習4
    key = "" #現在押されているキーを表す

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()