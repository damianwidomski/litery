def setup():
    size(400,400)
    textSize(60)
def draw():
    background(255)
    text("D", width/2-50, height/2)
    text("W", width/2+20, height/2)
    fill(100)
    print(mouseX,mouseY)
    if (mouseX>=155 and mouseX<=205 and mouseY>=147 and mouseY<=200):
        text("W", width/2+20, height/2)
        fill(100,255,100)
        if keyPressed:
            if keyCode == 39 and mouseX>=155 and mouseX<=205 and mouseY>=147 and mouseY<=200:
                fill(255, 0, 0)
                text("W", width/2+20, height/2)
                fill(155)
                print(keyCode)
    if keyPressed:
        fill(0)
        if key == 'W' or key == 'W':
            fill(0)
            text("W", width/2+20, height/2)
            fill(155)
    if keyPressed:
        fill(155)
        if key == 'D' or key == 'D':
            fill(0)
            text("D", width/2-50, height/2)
            fill(0)
    if (mouseX>=225 and mouseX<=260 and mouseY>=147 and mouseY<=200):
        text("D", width/2-50, height/2)
        fill(255, 102,255)
        if keyPressed:
            fill(155)
            if keyCode == 37 and mouseX>=225 and mouseX<=260 and mouseY>=147 and mouseY<=200:
                fill(0, 255, 0)
                text("D", width/2-50, height/2)
                fill(155)
                print(keyCode)
