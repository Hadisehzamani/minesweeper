from tkinter import Button
import random

class Cell:
    all = []
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            text= f'{self.x},{self.y}'
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print('left click')

    def right_click_actions(self, event):
        print('right click')
    
    @staticmethod
    def randomize():
        picked_cells = random.sample(Cell.all, 9)

        for x in picked_cells:
            x.is_mine = True

    def __repr__(self):
        return f'Cell({self.x,},{self.y})'
    
    