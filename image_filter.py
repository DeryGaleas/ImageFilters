import cv2

image = cv2.imread(r"puppet_master.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r"puppet_master_gray_skin.jpg", gray_image)

inverted_image = 255 - gray_image
cv2.imwrite(r"puppet_master_inverted_skin.jpg", inverted_image)

blurred_image = cv2.GaussianBlur(inverted_image, (21,21),0)
cv2.imwrite(r"puppet_master_blurred_skin.jpg", blurred_image)

inverted_blurred_image = 255 - blurred_image
pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
cv2.imwrite(r"puppet_master_inverted_blurred_skin.jpg", pencil_sketch)