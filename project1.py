import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle
t = turtle.Turtle()

# Hide the turtle
t.hideturtle()

# Set the speed (0 = fastest, 1 = slowest, 10 = fast)
t.speed(0)  # Using 0 for maximum speed since you're doing many iterations

# List of colors to cycle through
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw multiple circles
for i in range(10000000000):
    # Change color by cycling through the colors list
    current_color = colors[i % len(colors)]
    t.color(current_color)
    t.circle(100)
    t.right(1)

    



# Keep the window open
screen.mainloop()
