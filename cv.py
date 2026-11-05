# import os
# import cv2

# path = r"abhi.jpeg"  # Use raw string to avoid issues with backslashes

# # Debug check: confirm the file actually exists at this path
# print("File exists:", os.path.exists(path))

# img = cv2.imread(path)

# if img is None:
#     print("Image not found! Check the path above and OneDrive sync status.")
# else:
#     # Shape
#     print("Shape:", img.shape)

#     # Size — array element count (height x width x channels), NOT file size
#     print("Array Size (elements):", img.size)

#     # Actual memory/byte size of the array
#     print("Array Size (bytes):", img.nbytes)
#     print("Array Size (KB):", round(img.nbytes / 1024, 2))
#     print("Array Size (MB):", round(img.nbytes / (1024 * 1024), 2))

#     # Actual file size on disk (compressed, what you'd see in File Explorer)
#     file_size_bytes = os.path.getsize(path)
#     print("File Size on Disk (KB):", round(file_size_bytes / 1024, 2))
#     print("File Size on Disk (MB):", round(file_size_bytes / (1024 * 1024), 2))

#     # Data type
#     print("Data Type:", img.dtype)

#     # Height, Width, Channels (resolution)
#     height, width, channels = img.shape
#     print("Height:", height)
#     print("Width:", width)
#     print("Channels:", channels)
#     print(f"Resolution: {width} x {height}")

#     # Pixel access — img[y, x] returns [B, G, R] values at that coordinate
#     pixel = img[100, 50]  # row 100 (y), column 50 (x)
#     print("Pixel at (50, 100) [B, G, R]:", pixel)

#     b, g, r = img[100, 50]
#     print("Blue:", b, "Green:", g, "Red:", r)

#     # Modify a pixel — set it to pure red (B=0, G=0, R=255)
#     img[100, 50] = [0, 0, 255]
#     print("Pixel after modification:", img[100, 50])

#     # Convert to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Pixel access on grayscale image — just a single intensity value
#     gray_pixel = gray[100, 50]
#     print("Grayscale pixel at (50, 100):", gray_pixel)

#     print("Gray Shape:", gray.shape)  # no channels dimension now, just (height, width)
#     print("Gray Data Type:", gray.dtype)

#     # Resize before displaying, so the window matches the image exactly
#     resized = cv2.resize(gray, (800, 600))

#     # View and save the grayscale result
#     cv2.imshow("Grayscale", resized)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     cv2.imwrite("gray_output.png", gray)

#     # -----------------------------------------------------------
#     # Canny Edge Detection
#     # -----------------------------------------------------------
#     # Detects edges using two thresholds: pixels above the upper
#     # threshold are "strong" edges, pixels below the lower one are
#     # discarded, and pixels in between are kept only if connected
#     # to a strong edge. Works on the grayscale image.
#     canny_edges = cv2.Canny(gray, threshold1=100, threshold2=200)

#     canny_resized = cv2.resize(canny_edges, (800, 600))
#     cv2.imshow("Canny Edge Detection", canny_resized)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     cv2.imwrite("canny_output.png", canny_edges)

#     # -----------------------------------------------------------
#     # Sobel Edge Detection
#     # -----------------------------------------------------------
#     # Computes intensity gradients in the x and y directions
#     # separately, then combines them. Unlike Canny, it doesn't
#     # produce clean binary edges — it highlights gradient strength.
#     sobel_x = cv2.Sobel(gray, cv2.CV_64F, dx=1, dy=0, ksize=3)  # vertical edges
#     sobel_y = cv2.Sobel(gray, cv2.CV_64F, dx=0, dy=1, ksize=3)  # horizontal edges

#     # Convert back to uint8 for display/saving (Sobel output can be negative)
#     sobel_x_abs = cv2.convertScaleAbs(sobel_x)
#     sobel_y_abs = cv2.convertScaleAbs(sobel_y)

#     # Combine both directions into one edge map
#     sobel_combined = cv2.addWeighted(sobel_x_abs, 0.5, sobel_y_abs, 0.5, 0)

#     sobel_resized = cv2.resize(sobel_combined, (800, 600))
#     cv2.imshow("Sobel Edge Detection", sobel_resized)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     cv2.imwrite("sobel_x_output.png", sobel_x_abs)
#     cv2.imwrite("sobel_y_output.png", sobel_y_abs)
#     cv2.imwrite("sobel_combined_output.png", sobel_combined)

import cv2
img=cv2.imread("abhi.jpeg")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(grey,100,200)
cv2.imshow("Original",img)
cv2.imshow("Gray",grey)
cv2.imshow("Edges",edges)
cv2.waitKey(0)  
cv2.destroyAllWindows()