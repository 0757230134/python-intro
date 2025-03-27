from PIL import Image

img = Image.open('images/img cover.jpg')

img2 = img.convert('L')

img2.save('images/img cover2.jpg')