from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()        
        self.goto(-270, 260)
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", align="left",  font=FONT)

    def update_score(self):
        self.level+=1
        self.clear()
        self.write_score()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
