import cv2
# Read the image
image = cv2.imread('images/3.jpg')
print(image)

cv2.imshow('Imagen', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

