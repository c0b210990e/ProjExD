import tkinter as tk
import meiro as mm 
import random
import tkinter.messagebox as tkm

def key_down(event): 
    global key
    key = event.keysym

def key_up(event): 
    global key
    key = ""

#自分のこうかとん
def main_proc(): 
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

#敵のこうかとん
def teki_kokaton():
    global tx, ty
    global tcx, tcy
    work = random.randint(1,4)
    if work%4==0:
        ty -= 1
    elif work%4==1:
        ty += 1
    elif work%4==2:
        tx -= 1
    else:
        tx += 1
    if maze_list[ty][tx] == 0:
        tcx, tcy = tx*100+50, ty*100+50
    else:
        if work%4==0:
            ty += 1
        elif work%4==1:
            ty -= 1
        elif work%4==2:
            tx += 1
        else:
            tx -= 1
    canv.coords("t_tori",tcx,tcy)
    root.after(1000, teki_kokaton)

def teki_kokaton2():
    global gx, gy
    global gcx, gcy
    work = random.randint(1,4)
    if work%4 == 0:
        gy -= 1
    elif work%4 == 1:
        gy += 1
    elif work%4 == 2:
        gx -= 1
    else:
        gx += 1
    if maze_list[gy][gx] == 0:
        gcx, gcy = gx*100+50, gy*100+50
    else:
        if work%4 == 0:
            gy += 2
        elif work%4 == 1:
            gy -= 2
        elif work%4 == 2:
            gx += 2
        else:
            gx -= 2
    canv.coords("t_tori2", gcx, gcy)
    root.after(1000, teki_kokaton2)

def destroy():
    if t_tori[tx][ty] == tori[mx][my]:
        canv.delete(id1)

#タイマー機能(秒数がカウントアップされる)
def count_up():
    global tmr
    tmr += 1
    label["text"] = tmr
    root.after(1000, main_proc)
    #if tmr > 100:
    #    tkm.showerror("お知らせ", "Game Over")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("パックマンゲーム") 
    canv = tk.Canvas(root,width = 1500, height = 900, bg = "black") 
    
    canv.pack()
    label = tk.Label(root, font=("",80))
    label.pack()

    maze_list = mm.make_maze(15,9)
    print(maze_list) #1:壁/0:床を表す

    mm.show_maze(canv, maze_list)

    tori = tk.PhotoImage(file = "fig/6.png") 
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image = tori, tag = "tori")

    tx, ty = 4, 4
    tcx, tcy = tx*100+50, ty*100+50
    id1 = t_tori = tk.PhotoImage(file = "fig/5.png")            
    canv.create_image(tx, ty, image = t_tori, tag = "t_tori") 

    gx, gy = 10,5
    gcx, gcy = gx*100+50, gy*100+50
    t_tori2 = tk.PhotoImage(file = "fig/9.png")
    canv.create_image(gx, gy, image = t_tori2, tag = "t_tori2") 

    key = "" #現在押されているキーを表す

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    teki_kokaton()
    teki_kokaton2()

    tmr = 0
    root.after(1000, count_up)
    root.mainloop()

   

    