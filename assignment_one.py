# Owen Feng
# 10-22-22
import turtle

def draw_octagons(side_length, color):
    '''this fuction draw a octagons'''
    turtle.fillcolor(color)
    turtle.begin_fill()

    for x in range(8):
        turtle.forward(90)
        turtle.left(45)

    turtle.end_fill()

# calls the function
draw_octagons(100,"red")


#moves the pen
turtle.penup()
turtle.goto(-280,90)
turtle.pendown()

'''draw a second octagons'''

draw_octagons(100,"blue")

turtle.begin_fill()



turtle.end_fill()


turtle.penup()
turtle.goto(-230,-300)
turtle.pendown()

'''draw a third octagons'''

draw_octagons(100,"pink")


turtle.begin_fill()


turtle.end_fill()


turtle.penup()
turtle.goto(120,-300)
turtle.pendown()

'''draw a forth octagons'''

draw_octagons(100,"green")


turtle.end_fill()






turtle.exitonclick()



