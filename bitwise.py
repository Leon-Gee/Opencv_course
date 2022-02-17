import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)


#benn diagram 101
#thats why u mf need math

#intersection regions
#bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)


#both intersection and non intersection regions
#bitwise or
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise or', bitwise_or)


#only intersection regions
#bitwise xor 
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise xor', bitwise_xor)


#highlits the non filled regions
#bitwise not
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise not', bitwise_not)

cv.waitKey(0)
