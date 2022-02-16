import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

#plt.imshow(img)
#plt.show()


#BGR to GrayScale, not gray, GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L+a+b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)
#plt.imshow(rgb)
#plt.show()

#Lets do it, like, backwards ;)

#HSV 2 BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV TO BGR', hsv_bgr)


cv.waitKey(0)

