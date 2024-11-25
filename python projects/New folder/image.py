"""# Flipping the image

from PIL import Image
 #oppening the image
img = Image.open("C:/Users/surya/Downloads/download.jpg")
#img.show()

#transposing
transposed_img= img.transpose(Image.FLIP_LEFT_RIGHT)

#save it to a file in a human understandable format

transposed_img.save("flipped_image.webp")
print("Done flliping")   """

#image enhancement  CLANE
  
import cv2

#read the image

img= cv2.imread("C:/Users/surya/Downloads/download.jpg")


# preparation for CLANE

clahe=cv2.createCLAHE()

#convert to gray scale image

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#APPLY enhancement

enh_img=clahe.apply(gray_img)

# save it to a file human

cv2.imwrite("enhanced.png",enh_img)
print("Done enhancing")