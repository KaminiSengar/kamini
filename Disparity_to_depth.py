# Camera parameters from calibration (example values, replace with yours)
focal_length = 700  # in pixels
baseline = 0.2  # in meters (distance between cameras)

# Avoid division by zero (convert disparity to float)
disparity = np.float32(disparity)
disparity[disparity == 0] = 0.1  # Smallest nonzero disparity to prevent division error

# Compute depth
depth_map = (focal_length * baseline) / disparity

# Normalize for visualization
depth_visual = cv2.normalize(depth_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
depth_visual = np.uint8(depth_visual)

# Show depth map
cv2.imshow("Depth Map", depth_visual)
cv2.waitKey(0)
cv2.destroyAllWindows()
