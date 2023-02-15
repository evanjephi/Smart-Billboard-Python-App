from PIL import ImageTk, Image

with open('/home/pi/Pictures/Rings.png', 'rb') as f:
    image = f.read()
    
with open('/home/pi/Pictures/newTestlel.jpg', 'wb') as file:
        file.write(image)