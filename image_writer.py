from PIL import Image, ImageFont, ImageDraw

img = Image.open("tribal.jpg","r")
width,height = img.size
font = ImageFont.truetype("monaco.ttf",16)
draw = ImageDraw.Draw(img)
text_x,text_y= font.getsize("Tribal Ethiopia")
draw.text(((width-text_x)/2,(height-text_y)/2),"Tribal Ethiopia",(255,255,255),font=font)
img.save("branded.jpg")

