from PIL import Image,ImageDraw, ImageFont

img = Image.open('Images/img cover.jpg')
draw = ImageDraw.Draw(Image)

font = ImageFont.truetype('arial.ttf', 20)

text = "ForestView"

bbox = draw.textbbox((0,0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
image_width, image_height = img.size
x = (image_width - text_width) / 2
y = (image_height - text_height) / 2

draw.text((x, y), text,fill = "white", font = font)
img.show()
img.save('Images/img cover.jpg')