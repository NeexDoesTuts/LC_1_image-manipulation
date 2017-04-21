import image

img = image.Image("luther.jpg")
window = image.ImageWin(img.getWidth(), img.getHeight())

for row in range(img.getWidth()):
    for col in range(img.getHeight()):
        pixel = img.getPixel(row, col)
        green = pixel.getGreen()
        blue = pixel.getBlue()
        newpixel = image.Pixel(0, green, blue)
        img.setPixel(row, col, newpixel)

img.draw(window)
