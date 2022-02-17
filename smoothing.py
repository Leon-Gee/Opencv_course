import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')

cv.imshow('cats', img)

#average blur works this way
#you take a window in the image, the dimensions are the rows and the columns
#[][][Y]
#[][X][Y]
#[][Y][]
#The blur in the x pixel will become the average of the y pixels
#So we apply a average blur function to our image

average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)


#gaussianblur
#Gaussian blur works the same way as average blur, but not all pixel are equal the same in the average calculation
#instead, the surronding pixels gets a weight value, then, when the average calculation its beign made, the weight
# its the percentage applied into the function, giving us less blur than average, but its more natural.

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussianblur', gauss)

#medium blur
#same thing as average, but instead of using average uses the medium of the surrounding pixels

medium = cv.medianBlur(img,3)
cv.imshow('medium', medium)


#Bilateral
#the most effective
#Bilateral blur the images but it keeps the edges of the image 
bilateral = cv.bilateralFilter(img, 5, 35, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
