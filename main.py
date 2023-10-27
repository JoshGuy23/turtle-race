from turtle import Turtle, Screen


def start_race():
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_pos = -70

    for t in range(6):
        tim = Turtle(shape="turtle")
        tim.penup()
        tim.color(colors[t])
        tim.goto(x=-230, y=y_pos)
        y_pos += 30

    screen.exitonclick()


start_race()
