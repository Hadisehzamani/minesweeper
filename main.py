from tkinter import *
from cell import Cell
import setting
import utils

root = Tk()
root.configure(bg='black')
root.geometry('1440x720')

top_frame = Frame(
    root,
    bg='black',
    width=setting.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=setting.HEIGHT
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25),
)

for x in range(6):
    for y in range(6):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.randomize()

root.mainloop()