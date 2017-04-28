import cImage as image

img = image.Image("luther.jpg")
width = img.getWidth()
height = img.getHeight()
window = image.ImageWin("smooth", img.getWidth(), img.getHeight())

def average_pixel(col, row, img):
    pixel = img.getPixel(col,row)
    pixel_sum_red = 0
    pixel_sum_green = 0
    pixel_sum_blue = 0
    pixel_count = 0
    max_col = img.getWidth()
    max_row = img.getHeight()

    for i in range(col -1, col + 2):
        for j in range(row - 1, row + 2):
            if max_col > i >= 0 and max_row > j >= 0:
                pixel = img.getPixel(i,j)
                pixel_sum_red += pixel.getRed()
                pixel_sum_green += pixel.getGreen()
                pixel_sum_blue += pixel.getBlue()

                pixel_count += 1

    pixel.setRed(int(pixel_sum_red / pixel_count))
    pixel.setGreen(int(pixel_sum_green / pixel_count))
    pixel.setBlue(int(pixel_sum_blue / pixel_count))
    return pixel

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        new_pixel = average_pixel(col, row, img)
        img.setPixel(col,row, new_pixel)

img.draw(window)
window.exitonclick()