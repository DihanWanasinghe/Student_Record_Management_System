from graphics import *   #import the graphics.py module (must be in the same folder this file)


#OPEN THE WINDOW
win = GraphWin("My First Graphics Window", 800, 600)#open a window object called "win" with size and title 
win.setBackground("Mint Cream")# Set the background colour of the window

my_heading = Text(Point(100, 30), 'Here is My Heading')
my_heading.setTextColor("grey")
my_heading.setSize(24)
my_heading.setStyle("bold")
my_heading.setFace("helvetica")

# Render text to our window
my_heading.draw(win)










# Define some text
my_heading = Text(Point(100, 30), 'Here is My Heading')
my_heading.setTextColor("grey")
my_heading.setSize(24)
my_heading.setStyle("bold")
my_heading.setFace("helvetica")

# Render text to our window
my_heading.draw(win)

# Define a circle: center at 150px, 300px, radius is 100px
aCircle = Circle(Point(150, 300), 100)

# Render the circle to the window
aCircle.draw(win)

# Wait for a click to close the window









# Create a graphics window (assumed you're using the graphics library)


# Define the subheading and style it
my_sub_heading = Text(Point(140, 60), 'Here is My Subheading')  # Define the text
my_sub_heading.setTextColor("grey")
my_sub_heading.setSize(20)
my_sub_heading.setStyle("bold")
my_sub_heading.setFace("helvetica")

# Render the subheading to the window
my_sub_heading.draw(win)

# Define a second circle and set its properties
b_Circle = Circle(Point(400, 300), 120)
b_Circle.setFill("Lime")
b_Circle.setWidth(0)

# Render the circle to the window
b_Circle.draw(win)

# Wait for user input or close the window


