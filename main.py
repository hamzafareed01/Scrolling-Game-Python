###############################################################
#Name: Hamza Fareed Ahmed Syed

#Title: Scrolling Collision Game

#Description:
#A collision game where a player tries to avoid falling objects causing ‘harm’ and collect ‘points’ to move onto next level.
#As the level increases, the speed of the falling objects and players speed increases
#A harm and a benefit character move across the screen from top to bottom, and upon collision with the player will either reduce game lives or increase score.
#This project includes combination of blocks, conditional statements and loops.

###############################################################

#Import modules
#These are the required file packages
import turtle
import random

s = turtle.Screen()
s.screensize(500, 500)
s.setup(520, 520)

s.bgpic("Konoha_500x500.gif")
s.tracer(0)

width, height = s.screensize()
game = {
    "score": 0,
    "lives": 3,
    "level": 1,
    "frames": 0,
    "benefit_point_increase": 100,
    "level_increase_value": 200
}

harm = {
    "turtle": turtle.Turtle(),
    "radius": 20,
    "speed": 1,
    "type": "harm",
    "color": "red",
    "image": "dark-orb_50x50.gif"
}

chakra = {
    "turtle": turtle.Turtle(),
    "radius": 5 * 2,
    "speed": 1,
    "type": "chakra",
    "color": "blue",
    "image": "XDZT_50x50.gif"
}

player = {
    "turtle": turtle.Turtle(),
    "radius": 5 * 2,
    "speed": 10,
    "type": "player",
    "image": "naruto_80x80.gif",
    "color": "yellow"
}

#player["turtle"].hidetudtle()
player["turtle"].penup()
player["turtle"].goto((-width / 2), (-height / 2) + 50)
player["turtle"].color(player["color"])

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

for obj in [harm, chakra, player]:
    d_orb = obj["image"]

    s.addshape(d_orb)
    obj["turtle"].shape(d_orb)
    obj["turtle"].penup()

# # for harm/chakra, random start position
#   if (obj["type"] == "player"):
#     obj["turtle"].goto(-width/2 + 80, (-height/2))
#   else:
#     obj["turtle"].sety((height/2))
#     rand_x = random.randint(-(width/2), width/2)
#     obj["turtle"].setx(rand_x)

keep_animating = True


#define function
def move_right():
    t = player["turtle"]
    current_x = t.xcor()
    new_x = current_x + player["speed"]
    t.setx(new_x)


def move_left():
    t = player["turtle"]
    current_x = t.xcor()
    new_x = current_x - player["speed"]
    t.setx(new_x)


def write_game_data():

    writer.goto(240, 220)
    writer.write("LIVES: " + str(game["lives"]),
                 align="right",
                 font=("Arial", 18, "normal"))

    writer.goto(0, 220)
    writer.write("Level: " + str(game["level"]),
                 align="center",
                 font=("Arial", 18, "normal"))

    writer.goto(-240, 220)
    writer.write("Score: " + str(game["score"]),
                 align="left",
                 font=("Arial", 18, "normal"))


def are_colliding(obj1, obj2):

    result = False
    t1 = obj1["turtle"]
    t2 = obj2["turtle"]

    distance = t1.distance(t2)

    if (distance < obj1["radius"] + obj2["radius"]):
        result = True

    return result


#261241
def play_game():
    while (game["lives"] >= 1):
        #clear previous drawings
        for obj in [harm, chakra, player]:
            obj["turtle"].clear()

        writer.clear()

        #update values
        for obj in [harm, chakra]:
            current_pos = obj["turtle"].ycor()
            obj["turtle"].sety(current_pos - (obj["speed"] * game["level"]))

        game["frames"] += 1

        #handle any conditions
        for obj in [harm, chakra]:
            max_y = (height / 2) + obj["radius"]

            min_y = -(height / 2) - obj["radius"]

            if (obj["turtle"].ycor() <= min_y):

                obj["turtle"].sety(max_y)
                random_x = random.randint(-(width / 2), width / 2)
                obj["turtle"].setx(random_x)

        for obj in [harm, chakra]:
            if (are_colliding(obj, player)):

                obj["turtle"].sety(max_y)
                random_x = random.randint(-(width / 2), width / 2)
                obj["turtle"].setx(random_x)

                if (obj["type"] == "harm"):
                    game["lives"] -= 1
                elif (obj["type"] == "chakra"):
                    game["score"] += game["benefit_point_increase"]
                    #update level
                    if (game["score"] % game["level_increase_value"] == 0):
                        game["level"] += 1

        write_game_data()

        s.update()
    show_game_over_screen()


def show_start_screen():
    # print('okay')
    writer.color("red")
    writer.write("Instructions",
                 align="center",
                 font=("Copperplate Gothic Bold", 18, "bold"))
    writer.sety(writer.ycor() - 60)

    writer.write("Absorb blue chakra to win",
                 align="center",
                 font=("Arial", 18, "bold"))
    writer.sety(writer.ycor() - 60)

    writer.write("Press SPACE KEY to start",
                 align="center",
                 font=("Arial", 18, "bold"))
    writer.sety(writer.ycor() - 60)


def show_game_over_screen():
    for obj in [harm, chakra, player]:
        obj["turtle"].clear()

    s.update()

    writer.clear()
    writer.goto(0, 0)
    writer.color("red")
    writer.write("Game Over", align="center", font=("Arial", 18, "bold"))
    writer.sety(writer.ycor() - 40)
    writer.write("Score: " + str(game["score"]),
                 align="center",
                 font=("Arial", 18, "bold"))
    s.update()


def show_start_screen():
    # print('okay')
    writer.color("red")
    writer.write("Instructions",
                 align="center",
                 font=("Copperplate Gothic Bold", 18, "bold"))
    writer.sety(writer.ycor() - 60)

    writer.write("Absorb blue chakra to win",
                 align="center",
                 font=("Arial", 18, "bold"))
    writer.sety(writer.ycor() - 60)

    writer.write("Press SPACE KEY to start",
                 align="center",
                 font=("Arial", 18, "bold"))
    writer.sety(writer.ycor() - 60)


def main():
    show_start_screen()


s.onkeypress(move_right, "Right")
s.onkeypress(move_left, "Left")
s.onkeypress(play_game, "space")
print(move_right)
s.listen()

main()
