import cv2
import numpy as np

alphabet = "Ñ@#W$9876543210?!abc;:+=-,._ "

def my_resize(scale_percent, img, vbok):
	width = int(img.shape[1] * 1.5 * scale_percent / 100)
	if (vbok):
		height = int(img.shape[0])
	else:
		height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	return resized

def get_image(file = "./max.jpeg"):
	image = cv2.imread(file)
	#rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	return image

def show_image(image):
	cv2.imshow("Image", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def	encode_image(image):
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			x = image[i][j]
			brightness = (2 * x[0] + x[1] + 7 * x[2]) / 9
			charac = alphabet[28 - int(brightness * 29 / 255)]
			print(f"{charac}", end=" ")
		print("")

def main():
	im = get_image("./nastya.jpg")#[:650, ::]
	#print(im.shape)
	#show_image(im)
	n_im = my_resize(5, im, 0)
	encode_image(n_im)
	show_image(im)
	#cv2.imwrite("./max4.jpeg", im)
main()
