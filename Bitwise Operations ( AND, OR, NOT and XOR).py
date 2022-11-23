import cv2 as cv
import numpy as np 
#image 1
img1 = np.zeros ((250,500,3) , np.uint8)
img1 = cv.rectangle(img1, (200,0),(300,100), (255,255,255), -1)

# image 2
img2 = np.full((250,500,3) , 255,np.uint8 )
img2 = cv.rectangle(img2, (0,0), (250,250), (0,0,0), -1)



#bitAnd = cv.bitwise_and(img2 , img1)
# bitOr  = cv.bitwise_or(img2, img1)
# bitXor = cv.bitwise_xor(img1, img2)
bitNot1 = cv.bitwise_not(img1)
bitNot2 = cv.bitwise_not(img2)



cv.imshow('img1', img1)
cv.imshow('img2', img2)
#cv.imshow('bitAnd', bitAnd)
# cv.imshow('bitOr', bitOr)
# cv.imshow('bitXor', bitXor)
cv.imshow('bitNot1', bitNot1)
cv.imshow('bitNot2', bitNot2)



cv.waitKey(0)
cv.destroyAllWindows()

