import cv2

# Đọc một bức ảnh
img = cv2.imread("50.jpg", 1)

# Hiển thị ảnh
cv2.imshow("photo", img)

# Chờ phím được nhấn trong 100 mili giây
k = cv2.waitKey()
