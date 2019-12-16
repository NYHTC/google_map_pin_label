"""
Create files with a number inside the pin marker.

Original image taken from:
https://www.iconfinder.com/icons/322462/map_marker_icon
"""
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


colors = {'black': (0, 0, 0),
          'white': (255, 255, 255),
          'red': (237, 30, 36),
          'blue': (141, 213, 245),
          'green': (22, 155, 98),
          'yellow': (255, 207, 46)
          }
fonts = {'arial_nar': ImageFont.truetype("/Library/Fonts/Arial Narrow.ttf", 8),
         'arial': ImageFont.truetype("/Library/Fonts/Arial.ttf", 8),
         'arial_b': ImageFont.truetype("/Library/Fonts/Arial Black.ttf", 12),
         'monaco': ImageFont.truetype("/Library/Fonts/Monaco.dfont", 11)}
marker_colors = ['blue', 'red', 'yellow']
text_colors = {'blue': 'black',
               'red': 'white',
               'yellow': 'black'}


def replace_color(img, rgb_original, rgb_new):
    """Given an image and an color, return an image with the replaced color."""
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            if (r, g, b) == (rgb_original):
                pixels[x, y] = (rgb_new[0], rgb_new[1], rgb_new[2], a)
    return img


def add_text(img, font, rgb, text):
    """Given and image and font, add text to it."""
    img_w, img_h = img.size
    draw = ImageDraw.Draw(img)
    text_w, text_h = draw.textsize(text, font)
    draw.text((((img_w - text_w) / 2), 14),
              text, rgb, font=font)
    del draw
    return img


def create_images():
    """Create images all colors/numbers."""
    for color in marker_colors:
        print('generating {} markers'.format(color))

        # create dirs if needed
        color_path = os.path.join('images', color)
        if not os.path.exists(color_path):
            os.makedirs(color_path)

        # load template image and create a copy with a new color and label
        for i in range(2000):
            img = Image.open("images/pin_thin_" + color + "_48.png")
            # img = replace_color(img, colors['white'], colors[color])
            img = add_text(img, fonts['arial_b'], text_colors[color], str(i))
            save_path = os.path.join('images', color, str(i) + '.png')
            img.save(save_path)
    return True


if __name__ == '__main__':
    create_images()
