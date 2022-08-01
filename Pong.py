from turtle import Turtle,Screen
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9
    def reset(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,210)
        self.write(self.l_score,align="center",font=("Courier",60,"normal"))
        self.goto(100,210)
        self.write(self.r_score,align="center",font=("Courier",60,"normal"))
    def l_point(self):
        self.l_score+=1
        self.update()
    def r_point(self):
        self.r_score+=1
        self.update()
for n in range(-11,11):
    line=Turtle()
    line.shape="square"
    line.color("white")
    line.penup()
    line.shapesize(stretch_len=0.5,stretch_wid=3)
    line.goto(0,n*30)
r_paddle=Paddle((380,0))
l_paddle=Paddle((-380,0))
ball=Ball()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<80 and ball.xcor()>340 or ball.distance(l_paddle)<80 and ball.xcor()<-340:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.reset()
        scoreboard.r_point()












































screen.exitonclick()

