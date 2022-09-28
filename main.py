import pygame as pg
import sys
import random 
import time

pg.font.init()

def inp_rgb(text):
    col = input(text)
    col = col.strip()
    col = col.strip("(")
    col = col.strip(")")
    args = col.split(",")
    r = int(args[0])
    g = int(args[1])
    b = int(args[2])
    return [r,g,b]

img_path = input("Please enter the path to img: ")
font_path = input("Please enter the fontfile path: ")
font_size = int(input("Please enter font size: "))

bg_color = inp_rgb("Please enter background color in RGB: ")
text_color = [255,0,0]

if bg_color == text_color:
    text_color[0] = 123

"""
img_path = "pythonimg.png"
font_path = "font.otf"
font_size = 60

bg_color = (0,0,0)"""


with open("words.txt","r") as file:
    args = file.read()
    words = args.split(",")

original_img = pg.image.load(img_path)

new_img = pg.image.load(img_path)
text_surf  =pg.surface.Surface((original_img.get_size()))

text_surf.fill(bg_color)
new_img.set_colorkey(text_color)

font = pg.font.Font(font_path,font_size)

y_offset = 3
test = font.render("AAA",False,text_color)
line_height = test.get_height() + y_offset

needed_lines = original_img.get_height() // line_height + 3

currenty = 0
st = time.time()
for y in range(needed_lines):
    currentx = random.randint(0,50)
    while True:
        word = words[random.randint(0,len(words)-1)] + " "
        surf = font.render(word,False,text_color)
        surf_width = surf.get_width() 
        text_surf.blit(surf,(currentx,currenty))

        #pg.draw.rect(text_surf,"red",(currentx,currenty,surf_width,surf.get_height()),1)
        #pg.draw.circle(text_surf,"blue",(currentx,currenty),4)
        
        currentx += surf_width + random.randint(5,30)
        if currentx > original_img.get_width() + 30:
            currenty += surf.get_height()
            break
print("it took {} seconds to draw sprites".format(time.time()-st))

text_surf.set_colorkey(text_color)
new_img.blit(text_surf,(0,0))
pg.image.save(new_img,"result.png")
print("finished, saved result")

FLAGS = pg.RESIZABLE
screen = pg.display.set_mode((600,600),FLAGS)
clock = pg.time.Clock()

while True:
    screen.fill("black")
    clock.tick(60)   

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    s = pg.transform.scale(new_img,screen.get_size())
    screen.blit(s,(0,0)) 
    # when I pass screen as 3rd argument in transform.scale func 
    # the palette seems to bug out and replace blue with yellow and yellow with blue 
    # idk why that happens but it happens

    pg.display.update()
