from PIL import Image
import requests

im=Image.open("Carl_Evans.jpg")

w=128
h=128
im=im.resize((w,h), Image.ANTIALIAS)


pixels = list(im.getdata())
x = y = 0

for val in pixels:
    color = "#"
    for num in val:
        h = hex(num)[2:].upper()
        if (len(h) == 1):
            h = '0' + h
        color += h;
    print(color)
    requests.post('http://pixel.acm.illinois.edu', headers={'x': str(x), 'y': str(y), 'color': color})
    x+=1
    if(x > 127):
        x = 0
        y+=1

