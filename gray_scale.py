import cImage as image

img = image.Image("luther.jpg")
window = image.ImageWin("gray", img.getWidth(), img.getHeight())

for row in range(img.getWidth()):
    for col in range(img.getHeight()):
        pixel = img.getPixel(row, col)

        red = pixel.getRed()
        green = pixel.getGreen()
        blue = pixel.getBlue()
        gray = int(0.2989 * red + 0.5870 * green + 0.1140 * blue)

        newpixel = image.Pixel(gray,gray,gray)
        img.setPixel(row, col, newpixel)

img.draw(window)
window.exitonclick()