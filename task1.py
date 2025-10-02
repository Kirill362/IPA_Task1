from PIL import Image


def RGB_to_HSV(r, g, b):
    r, g, b = r/255, g/255, b/255
    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min

    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * ((b - r) / delta + 2)
    elif c_max == b:
        h = 60 * ((r - g) / delta + 4)

    if c_max == 0:
        s = 0
    else: s = delta / c_max

    v = c_max
    return h, s, v


if __name__ == '__main__':
    image = Image.open("img/RGB_image.jpg").convert("RGB")
    image.show()
    pixels = image.load()

    width, height = image.size
    hsv_image = Image.new("RGB", (width, height))
    hsv_pixels = hsv_image.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            h, s, v = RGB_to_HSV(r, g, b)
            hsv_pixels[x, y] = (int(h*255), int(s*255), int(v*255))

    hsv_image.save("img/output_hsv.jpg")
    hsv_image.show()
