grid_height = 30
grid_width = 60


block_size = 10
block_height = 5

noise_scale = .05
noise_multiplier = 100
noise_dampener = 2

image_border_buff = 5

w = grid_width * block_size + grid_height * block_size + image_border_buff * block_size
h = grid_height * block_size/2 + grid_width * block_size/2 + (int(noise(0,0) * noise_multiplier) / noise_dampener * block_height) + image_border_buff * block_size

start_block_x = w/2 - grid_height/2 * block_size + grid_width/2 * block_size 
start_block_y = h/2 - grid_height/2 * block_size/2 - grid_width/2 * block_size/2 + (int(noise(0,0) * noise_multiplier) / noise_dampener * block_height/2)

def draw_block(x,y):
    
    # Top Face
    beginShape()
    vertex(x - block_size, y)
    vertex(x, y - block_size/2)
    vertex(x + block_size, y)
    vertex(x, y + block_size/2)
    endShape(CLOSE)
    
    #Left Face
    beginShape()
    vertex(x - block_size, y)
    vertex(x, y + block_size/2)
    vertex(x, y + block_height + block_size/2)
    vertex(x - block_size, y + block_height)
    endShape(CLOSE)
    
    # Right Face
    beginShape()
    vertex(x + block_size, y)
    vertex(x, y + block_size/2)
    vertex(x, y + block_height + block_size/2)
    vertex(x + block_size, y + block_height)
    endShape(CLOSE)


def setup():
     size(w, h)
     draw_block(250, 250)
     
     for x in range(grid_height):
         for y in range(grid_width):
             
             cubes = int(noise(x * noise_scale, y * noise_scale) * noise_multiplier)
             draw_block((start_block_x + x * block_size) - y * block_size, (start_block_y + x * (block_size/2)) + y * (block_size/2))
     
