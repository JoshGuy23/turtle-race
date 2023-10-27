from turtle import Turtle, Screen
import random


def race(dist, racer):
    racer.forward(dist)


def start_race():
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle_list = []
    y_pos = -70

    for t in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[t])
        new_turtle.goto(x=-230, y=y_pos)
        y_pos += 30
        turtle_list.append(new_turtle)

    racing = True
    while racing:
        for race_turtle in turtle_list:
            if race_turtle.xcor() > 230:
                racing = False
                win_color = race_turtle.pencolor()
                if win_color == user_bet:
                    print(f"You win! The {win_color} turtle won the race!")
                else:
                    print(f"You lose. The {win_color} turtle won the race.")
                break
            race(dist=random.randint(0, 10), racer=race_turtle)

    screen.exitonclick()


start_race()
