import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Grayscale histogram
gray_histogram = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_histogram)
plt.show()

cv.waitKey(0)

