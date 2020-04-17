import turtle
import time
import random


delay = 0.1

#Score
score = 0
high_score = 0
#Setting up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600 , height=600)
window.tracer(0) #turns off screen updates

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments =[]

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
#Main game loop
while True:
    window.update()

    #Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #Clear the segment list
        segments.clear()

        #reset the score
        score = 0

        #Reset the delay
        delay = 0.1

        #update score display
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    #Check for collision with food
    if head.distance(food)< 20:
        #Move the food to random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.001

        #Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #Move the end segments first in reverse
    for index in range(len(segments)-1, 0 , -1):
        x = segments[index-1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #check for head collision with body segment
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            #Clear the segment list
            segments.clear()

            #reset the score
            score = 0

            #Reset the delay
            delay = 0.1

            #update score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

window.mainloop()