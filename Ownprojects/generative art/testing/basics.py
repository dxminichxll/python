import cairo, PIL, argparse, math, random

width, height = 3000, 2000

r, g, b = 0.3, 0.6, 0.6

ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
cr = cairo.Context(ims)

cr.set_source_rgb(r, g, b)
cr.rectangle(0, 0, width, height)
# ^^ creates a rectangle that starts at 0, 0 (top left corner) and draws to the bottom right corner
cr.fill()

def draw_line(r, g, b, startx, starty, endx, endy):
    cr.set_source_rgb(r,g,b)
    cr.set_line_width(2)
    cr.move_to(startx, starty)
    cr.line_to(endx, endy)
    cr.stroke()


# for i in range(100):
#     draw_line(1, 1, 1, 0, 0, i*100 ,2000)

# draw_line(1, 0, 0, 0, 0, 3000, 2000)
# draw_line(1, 0, 0, 3000, 0, 0, 2000)

for i in range(100):
    draw_line(1, 1, 1, 0, i**2, 3000, i**2)




ims.write_to_png('Generative-Space-Flat.png')
