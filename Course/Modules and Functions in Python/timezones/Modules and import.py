done = "drawing finished"
# This variable will be overwritten by the turtle function
from turtle import forward, done
import turtle

forward(150)
turtle.right(250)
forward(150)
done()

print(done)
# This is a problem when importing functions, you cannot use some variables becuase they are a function.
# This can be overcome by using the module name and "." when needed. For example, "turtle.done()" instead of "done"
