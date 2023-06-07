from turtle import Turtle, Screen
starting_position = [(0, 0), (-20, 0), (-40, 0)]


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
timmy = []

for position in range(0, 3):
    new_tim = Turtle("square")
    new_tim.color("white")
    new_tim.penup()
    new_tim.goto(starting_position[position])
    timmy.append(new_tim)


should_continue = True
while should_continue:
    screen.update()
    for tim_num in range(len(timmy) - 1, 0, -1):
        new_x = timmy[tim_num-1].xcor()
        new_y = timmy[tim_num-1].ycor()
        timmy[tim_num].goto(new_x, new_y)
    timmy[0].forward(5)
    timmy[0].left(5)


screen.exitonclick()
