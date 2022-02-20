import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

#simple threshholding

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# adaptative thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11, 3)
cv.imshow('Adaptative tresholding', adaptive_thresh)

cv.waitKey(0)
