import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed
pen.width(2)

# Number of colors in the spiral
n = 200

# Create a colorful spiral using hues from the HSV color model
for i in range(n):
    color = colorsys.hsv_to_rgb(i/n, 1.0, 1.0)  # Generate color from hue
    pen.color(color)  # Set the pen color

    pen.forward(i * 2)  # Move forward
    pen.left(59)  # Turn the turtle to create a spiral

# Hide the turtle when done
pen.hideturtle()

# Finish the drawing
turtle.done()
