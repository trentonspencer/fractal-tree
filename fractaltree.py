import math
import time
from tkinter import *

root = Tk()
root.configure(width=800, height=600)
root.title('Fractal Tree')

canvas_width = 80
canvas_height = 40
canvas = Canvas(root, width=800, height=600)
canvas.pack()

def doTree(x, y, bs, scale, rot, rinc, iters, citer=0):
    if citer > iters or (int(bs*scale) == 0):
        return

    sr = rot + (rinc * (citer > 0))
    rad = sr*3.14159/180
    sx = (bs*math.cos(rad)-bs*math.sin(rad))+x
    sy = (bs*math.cos(rad)+bs*math.sin(rad))+y
    canvas.create_line(x, y, sx, sy, fill="black")
    #time.sleep(0.05 + (citer * 2))
    doTree(sx, sy, bs * scale, scale, sr, rinc, iters, citer + 1)
    #root.after(200+(citer*2), doTree, sx, sy, bs * scale, scale, sr, rinc, iters, citer + 1)

    sr = rot - (rinc * (citer > 0))
    rad = sr*3.14159/180
    sx = (bs*math.cos(rad)-bs*math.sin(rad))+x
    sy = (bs*math.cos(rad)+bs*math.sin(rad))+y
    canvas.create_line(x, y, sx, sy, fill="black")
    #time.sleep(0.05+(citer*2))
    doTree(sx, sy, bs*scale, scale, sr, rinc, iters, citer+1)
    #root.after(200+(citer*2), doTree, sx, sy, bs*scale, scale, sr, rinc, iters, citer+1)

def smoothDraw(x, y, rad, bs, line, citer, cbs=0):
    if cbs > bs:
        sx = (bs * math.cos(rad) - bs * math.sin(rad)) + x
        sy = (bs * math.cos(rad) + bs * math.sin(rad)) + y
        canvas.coords(line, x, y, sx, sy)
        return
    sx = (cbs*math.cos(rad)-cbs*math.sin(rad))+x
    sy = (cbs*math.cos(rad)+cbs*math.sin(rad))+y
    canvas.coords(line, x, y, sx, sy)
    root.after(25, smoothDraw, x, y, rad, bs, line, citer, cbs+1)
    #time.sleep(0.05)
    #smoothDraw(x, y, rad, bs, line, cbs+1)

def doSmoothTree(x, y, bs, scale, rot, rinc, iters, citer=0):
    if citer > iters or (int(bs*scale) == 0):
        return

    sr = rot + (rinc * (citer > 0))
    rad = sr*3.14159/180
    sx = (bs*math.cos(rad)-bs*math.sin(rad))+x
    sy = (bs*math.cos(rad)+bs*math.sin(rad))+y
    smoothDraw(x, y, rad, bs, canvas.create_line(x, y, sx, sy, fill='black'), citer, 1)
    root.after(int(citer+(25 * bs)), doSmoothTree, sx, sy, bs * scale, scale, sr, rinc, iters, citer + 1)

    sr = rot - (rinc * (citer > 0))
    rad = sr*3.14159/180
    sx = (bs*math.cos(rad)-bs*math.sin(rad))+x
    sy = (bs*math.cos(rad)+bs*math.sin(rad))+y
    smoothDraw(x, y, rad, bs, canvas.create_line(x, y, sx, sy, fill='black'), citer, 1)
    root.after(int(citer+(25*bs)), doSmoothTree, sx, sy, bs*scale, scale, sr, rinc, iters, citer+1)

root.after(0, doSmoothTree, 400, 500, 30, 0.9, 225, 30, 8)
#root.after(0, doTree, 400, 500, 30, 0.9, 225, 30, 15)
root.mainloop()
