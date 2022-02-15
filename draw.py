import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')

cv.imshow('Blank', blank)

# 1 point the image a certain colour
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('square', blank)


#2 draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]),(0,255,0), thickness = 2)
cv.imshow('rectangle', blank)


# now a circle!
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40,(0,0,255), thickness = 1)
cv.imshow('circle', blank)

#A LINE!
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255), thickness = 3) 
cv.imshow('line', blank)
cv.waitKey(0)

