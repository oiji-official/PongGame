from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.display()
        

    def lpoint(self):
        self.lscore +=1
        self.display()

    def rpoint(self):
        self.rscore +=1
        self.display()

    def display(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))
