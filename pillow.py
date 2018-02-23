from PIL import Image, ImageDraw
import math
import numpy as np

im = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
draw = ImageDraw.Draw(im, "RGBA")
cx = im.size[0]
cy = im.size[1]
circleSize = 10
radius = 100
sRadius = radius*radius


for x in range(radius):
    y = int(math.sqrt(sRadius - x*x))
    x0 = x - circleSize
    y0 = y - circleSize
    x1 = x + circleSize
    y1 = y + circleSize
    coord0 = [cx + x0, cy + y0, cx + x1, cy + y1]
    draw.ellipse(coord0, fill=(255, 255, 255, 0), outline=(255, 0, 0, 255))
    coord0 = [cx - x0, cy + y0, cx - x1, cy + y1]
    draw.ellipse(coord0, fill=(255, 255, 255, 255), outline=(255, 0, 0, 255))
    coord0 = [cx + x0, cy - y0, cx + x1, cy - y1]
    draw.ellipse(coord0, fill=(255, 255, 255, 255), outline=(255, 0, 0, 255))
    coord0 = [cx - x0, cy - y0, cx - x1, cy - y1]
    draw.ellipse(coord0, fill=(255, 255, 255, 255), outline=(255, 0, 0, 255))


im.save("image.png", "PNG")
