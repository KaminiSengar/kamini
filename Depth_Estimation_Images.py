import cv2
import numpy as np

# Load stereo image pair
left_img = cv2.imread('left.jpg')  # Modify with your image path
right_img = cv2.imread('right.jpg')

# Convert to grayscale
gray_left = cv2.cvtColor(left_img, cv2.COLOR_BGR2GRAY)
gray_right = cv2.cvtColor(right_img, cv2.COLOR_BGR2GRAY)

# Set StereoBM parameters
stereo = cv2.StereoBM_create(numDisparities=64, blockSize=15)

# Compute disparity map
disparity = stereo.compute(gray_left, gray_right)

# Normalize for visualization
disparity_visual = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
disparity_visual = np.uint8(disparity_visual)

# Display results
cv2.imshow("Left Image", left_img)
cv2.imshow("Right Image", right_img)
cv2.imshow("Disparity Map", disparity_visual)
cv2.waitKey(0)
cv2.destroyAllWindows()
