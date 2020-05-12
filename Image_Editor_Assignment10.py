#!/usr/bin/env python3
"""
Created on Thur May  7 14:10:53 2020

@author: clinton potter
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, sys


##############################################################################
'''Takes user input to define image file, then asks user to choose from a set
of three programs'''
##############################################################################
def imageEditor():
	im = input('Please input your file name: ')
	pChoice = input('Please enter 1-3 to choose from the following programs: \n 1.) Meme Generator \n 2.) Image Rotater \n 3.) Image Tracer')

	if pChoice == '1':
		memeGen(im)
	elif pChoice == '2':
		rotater(im)
	elif pChoice == '3':
		contour(im)
	else:
		pChoice =input('Please enter a number 1-3')


##############################################################################
'''Takes user input to overlay text on image. It appropriately sizes the text
and centers it'''
##############################################################################
def memeGen(im):
	im = Image.open(im)
	message = input('''What would you like you're meme to say?''')
	draw = ImageDraw.Draw(im)
	imW, imH = im.size
	bounding_box = [imW/8, imH/8, (7*imW)/8, (7*imH)/8] #bounding box for text with 1/8th margins
	x1, y1, x2, y2 = bounding_box

	fontsFolder = '/Library/Fonts'
	startSize = int(imH/10) #starting point for text size loop

	for size in range(startSize,-1,-1):
	#for loop figures out the largest font size possible for the entered text
		arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), size)
		w,h = draw.textsize(message, font = arialFont) #gets size of text for given size
	
		if w < (x2-x1) and h < (y2-y1):
		#checks if text size fits in bounding box
			print('font size = ' + str(size))
			break
		elif size == 1:
		#if the text needed to be bigger than startSize, it defaults to startSize
			size = startSize

	x = (x2-x1-w)/2 +x1 #centers text width
	y = (y2-y1-h)/2 +y1 #centers text height

	draw.text((x,y), message, align = 'center', font = arialFont)

	im.save('meme.png')
	print('File saved as meme.png')
#############################################################################
"""Rotates image based on user defined input, loops until a proper integer is entered"""
#############################################################################
def rotater(im):
	im = Image.open(im)
	degrees = (input('''How many degrees would you like the image rotated? '''))

	while True:
		try:
			isinstance(int(degrees), int) == True #checks if user entered int type
			degrees = int(degrees)
			break
		except ValueError:
			degrees = (input('''Please enter an integer '''))

	im.rotate(degrees,expand=True).save('rotatedpic.png')
	print('File saved as ratatedpic.png')
##############################################################################
''' Uses the contour funtion from Pillow module to trace photo'''
##############################################################################
def contour(im):
	from PIL.ImageFilter import CONTOUR
	im = Image.open(im)

	im.filter(CONTOUR).save('traced_pic.png')

	print('\n','File saved as traced_pic.png')

imageEditor()
