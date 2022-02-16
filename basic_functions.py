import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Boston', img)




#The most important thing about image processing is to minimialize
#the quantity of data than is storaged in an image, this way we can
#process more quantity and get a most accurate result, thats why we are turning
# everything into gray scale


#converting to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)


#blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade
cany = cv.Canny(blur, 125, 175)
cv.imshow('Canny', cany)

#dilating thge image
dilated = cv.dilate(cany, (5,5), iterations = 4)
cv.imshow('Dilated edges', dilated)

#erading
eroded = cv.erode(dilated, (3,3), iterations = 2)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
