import cImage as image

img = image.Image("images/luther.jpg")
width = img.getWidth()
height = img.getHeight()
win = image.ImageWin("double", img.getWidth()*2, img.getHeight()*2)

img_double = image.EmptyImage(width*2,height*2)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        pixel = img.getPixel(col, row)

        c_pos = col * 2
        r_pos = row * 2
        img_double.setPixel(c_pos, r_pos, pixel)
        img_double.setPixel(c_pos+1, r_pos, pixel)
        img_double.setPixel(c_pos, r_pos+1, pixel)
        img_double.setPixel(c_pos+1, r_pos+1, pixel)

img_double.draw(win)
win.exitonclick()
