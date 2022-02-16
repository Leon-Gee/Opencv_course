import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Boston', img)

#translation
def translate(img, x , y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)


# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100,100)
cv.imshow('Translated', translated)


#rotation
def rotate(img, angle, rotation_point=None):
    (height, width) = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width//2, height//2)

    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotation_matrix, dimensions)

rotated_img = rotate(img, 45)
cv.imshow('Rotated', rotated_img)

rotated_rotated_img_2 = rotate(rotated_img, -45)
cv.imshow('Rotated rotated', rotated_rotated_img_2)


#resizing again, this is like the third time 4 real
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('resized HD', resized)


#flip flip
flip = cv.flip(img, 0)
cv.imshow('flipped', flip)


#cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)



cv.waitKey(0)
