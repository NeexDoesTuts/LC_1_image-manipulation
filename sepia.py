import cImage as image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
window = image.ImageWin("sepia", img.getWidth(), img.getHeight())

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()

        newred = int((red * 0.393 + green * 0.769 + blue * 0.189))
        newgreen = int((red * 0.349 + green * 0.686 + blue * 0.168))
        newblue = int((red * 0.272 + green * 0.534 + blue * 0.131))

        newpixel = image.Pixel(newred, newgreen, newblue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(window)
window.exitonclick()
