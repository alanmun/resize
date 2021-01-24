import PIL
import os
from PIL import Image

print("Welcome. This script will resize all images you have in a folder called \"resizeme\" to whatever width and height you desire.")
x = input('Enter the image width: ')
y = input('Enter the image height: ')

try:
	folder = os.getcwd() + r'/resizeme'
	os.listdir(folder)
except FileNotFoundError:
	print("Error: You need to put any images you wish to resize in a folder called \"resizeme\", in the same directory you executed this script from.")
	exit()
try:
	for filename in os.listdir(folder):
		f_img = folder+"/"+filename
		img = Image.open(f_img)
		img = img.resize((int(x),int(y)))
		img.save(f_img[0:-4]+"_" + str(x) + "x" + str(y) + ".png")
except:
	print("Some weird shit happened and execution has failed lol. Maybe one or more images is corrupted or not even an image. Make sure the folder only contains images")