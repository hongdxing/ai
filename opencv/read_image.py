

import cv2

image = cv2.imread('./images/input-image-for-demo-throughout-1024x682.jpeg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Cotton', image)
cv2.waitKey(0)

#cv2.imwrite('./images/copy.jpeg', image)

cv2.destroyAllWindows()

