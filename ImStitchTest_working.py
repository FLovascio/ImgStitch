#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import numpy as np

#X and Y are actually reversed

def makeImList(Name,xN,yN): 
#Name is the prefix in common between all the images whereas N is the number of images
    File_Array=[]
    X=0
    Y=0
    for i in range(xN):
        temparray = []
        for j in range(yN):
            I=(i+1)
            J=(j+1)
            #Some images are missing so I skip them, this leads to a bad final result.
            #It would probably be better to fill the spaces with black boxes of the correct size.
            #This should be quite straight forward, using Image.new()
            try:
                im=Image.open(Name+'_'+ f'{J:02}' + 'x' + f'{I:02}' + '.bmp')
                temparray.append(im)
            except:
                print('File '+Name+'_'+ f'{J:02}' + 'x' + f'{I:02}' + '.bmp'+' Is missing')
        File_Array.append(temparray)
    #Here I calculate the total image size    
    for image in File_Array[0][:]:
        width,height=image.size
        X+=width
    for image in File_Array[:][0]:
        width,height=image.size
        Y+=height
    return X,Y,File_Array

#Makes a new image with the read images 
def StitchImageList(X,Y,List):
#The inputs here are as the outputs from the previous function
    #create a new blanc image of the correct size (this will be BIG)
    new_im = Image.new('RGB', (X, Y))
    currentX=0
    currentY=0
    for row in List:
        currentX=row[0].size[0]
        for image in row:
            #Pasting in the images in order
            #The X direction seems to be reversed?
            new_im.paste(image, (X-currentX, currentY))
            currentX += image.size[0]
            print(currentX, currentY)
        currentY+=row[0].size[1]        
    return new_im


#Here you set name of immages and number
width,height,images=makeImList('2022090010', 12,12)

image=StitchImageList(width,height,images)

#I recommend against using image.show(), it crashed my computer.

image.save("BIG_IMG.bmp")
#The output is BIG and will take long to save and later open



