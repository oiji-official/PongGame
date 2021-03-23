from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        #no need to use line paddle = Turtle as turtle class has been inherited
        #self.paddle = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len= 1)
        self.penup()
        self.goto(pos)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor() , new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor() , new_y)