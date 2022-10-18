import tkinter as tk
import maze_maker as mm #練習8

def key_down(event): #練習5
    global key
    key = event.keysym
    root.after(1000,count_up)

def key_up(event): #練習6
    global key
    key = ""


def main_proc(): #練習7
    global tmr
    global mx, my 
    global cx, cy    
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_list[my][mx] == 0: #床だったら
        cx, cy = mx*100+50, my*100+50
    else: #壁だったら
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
        tmr += 10 #タイマーの秒数を10増やす
    canv.coords("tori", cx, cy)
    root.after(100,main_proc)

def count_up():
    global tmr
    tmr += 1
    label["text"] = tmr
    root.after(1000,count_up)
     

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1
    canv = tk.Canvas(root,width = 1500, height = 900, bg = "black") #練習2
    
    canv.pack()
    label = tk.Label(root, font=("",80))
    label.pack()

    #練習9
    maze_list = mm.make_maze(15,9)
    print(maze_list) #1:壁/0:床を表す

    #練習10
    mm.show_maze(canv, maze_list)

    tori = tk.PhotoImage(file="fig/6.png") #練習3
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image = tori, tag="tori")
    

    #練習4
    key = "" #現在押されているキーを表す

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()

    tmr = 0
    root.after(1000, count_up)
    root.mainloop()