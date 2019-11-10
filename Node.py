class Node:
    x_position=0
    y_position=0
    weight=0

    def __init__(self,x,y,w):
        self.x_position=x
        self.y_position=y
        self.weight=w

class Label:
    label=0
    vertex=0

    def __init__(self,lbl,vertex):
        self.label=lbl
        self.vertex=vertex
