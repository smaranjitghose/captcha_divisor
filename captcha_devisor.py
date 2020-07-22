from PIL import ImageFont, ImageDraw, Image
import numpy as np
import random 
import cv2
import string
import glob

#### Creating our canvas

size = random.randint(10, 16) 
length = random.randint(4, 8)
img = np.zeros(((size*2)+5, length*size, 3), np.uint8)
# The brightness has values between 0 (darkest) and 255 (brightest).
# By Default we get the darkest one (i.e. a black background) as we use (0,0,0)
# We add 255 to get the maximum brightness, i.e. a white background
img_pil = Image.fromarray(img+255) # Create the image out of the array

#### Drawing text and lines

draw = ImageDraw.Draw(img_pil) # Creating a drawing interface
# Path for our fonts
f_path = r'fonts/'
# Fetching all the true type format fonts from the given path
fonts = glob.glob(f_path+'*.ttf') 
# Randomy choosing a font from the tha path
font = ImageFont.truetype(random.choice(fonts), size)
# Generate random sequence of alpha numeric characters
text = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)for _ in range(length))
# Put the text with the random choice of characters,color,and font   
draw.text((5, 10), text, font=font,fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
# Draw lines with random start,end coordinates and filled with a random choice of color
draw.line([(random.choice(range(length*size)), random.choice(range((size*2)+5))), (random.choice(range(length*size)),
                                                                                   random.choice(range((size*2)+5)))], width=1, fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#### Adding noise 
img = np.array(img_pil)
# Select the threshold between 1% and 5%
threshold = random.randint(1, 5)/100 
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        rdn = random.random()
        if rdn < threshold: 
            img[i][j] = random.randint(0, 123) # dark pixels
        elif rdn > 1-threshold:
            img[i][j] = random.randint(123, 255) # white pixels

#### Blurring the image
img = cv2.blur(img, (int(size/random.randint(5, 10)),int(size/random.randint(5, 10))))


#create windows to display images
cv2.imshow('Captcha Devisor',img)
# Input keypress
k = cv2.waitKey(0) & 0xff
# If Esc key is pressed
if k == ord('q'):
    # Save the image in the desired path
    cv2.imwrite(f"assets/captcha.png", img)
    #close all the opened windows
    cv2.destroyAllWindows()
