#Dot Spot Painting#
import turtle as turtle_module
import random
turtle_module.colormode(255)
gavi = turtle_module.Turtle()
gavi.speed("fastest")
gavi.penup()
gavi.hideturtle()



color_list = [(237, 222, 85), (231, 170, 98), (193, 227, 243), (252, 53, 12), (239, 49, 85), (156, 84, 28), (172, 59, 112), (59, 179, 227), (85, 204, 147), (110, 216, 248), (22, 127, 214), (24, 183, 216), (237, 130, 161), (43, 112, 38), (36, 84, 43), (131, 234, 211), (252, 136, 142), (87, 29, 37), (250, 235, 239), (68, 162, 33), (99, 43, 22), (253, 221, 1), (105, 47, 27), (98, 37, 45), (38, 69, 44), (169, 132, 21), (234, 162, 157), (76, 130, 187)]

gavi.setheading(225)
gavi.forward(300)
gavi.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    gavi.dot(20, random.choice(color_list))
    gavi.forward(50)

    if dot_count % 10 == 0:
        gavi.setheading(90)
        gavi.forward(50)
        gavi.setheading(180)
        gavi.forward(500)
        gavi.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
