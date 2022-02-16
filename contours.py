import cv2 as cv
import numpy as np


img = cv.imread('Resources/Photos/cats.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#we create a blank image so we can draw the contorns we get from our contour function
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)



canny = cv.Canny(blur, 125,175)
#cv.imshow('Canny edges', canny)

#Treshing image, we get less contours than using blur and canning images
#treshing images its not always the most useful and viable method, in most cases
#its better to just blur and can the images


ret, tresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Tresh cats', tresh)

contours, hierarchies = cv.findContours(tresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
