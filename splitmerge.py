import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park',img)

#splitting
b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red', red)

#merging
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)


cv.waitKey(0)
