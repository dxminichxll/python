def setup():
    size(1000,1000)
    background(255, 255, 255)
    


    for c in range(50):
    
        
        center_x = random(200, 800)
        center_y = random(200, 800)
        cs = 150
        
        # Draw shadow
        noStroke()
        fill(15, 15, 15, 10)
        for i in range(30):
            circle(center_x, center_y, cs - i*5)
        
        # Draw circle
        stroke(30, 30, 30)
        fill(random(100, 255), random(100, 255), random(200, 255))
        circle(center_x - 25, center_y - 25, cs)
    
    save("shadow.png")
    
