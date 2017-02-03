#!/usr/bin/python
#Winston Venderbush


def isEven(num):
	return not num&1

def genImage(x, y):
	img = open("image.ppm", "w+")

	img.write("P3\n" + str(x) + " " + str(y) + "\n255\n\n");

	for ycor in range(0, y):
		for xcor in range(0, x):
			if isEven(xcor):
				img.write("255 255 0 ")
			else:
				img.write("0 255 0 ")
	img.write("\n")
	img.close()

genImage(750, 750)
