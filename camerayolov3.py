import cv2
import lYolo as ly

# Khởi tạo đối tượng LYLO
obj = ly.LYL()

# Mở camera
cap = cv2.VideoCapture(0)  # Số 0 thường tương ứng với camera mặc định

while True:
    # Đọc frame từ camera
    ret, frame = cap.read()
    if not ret:
        break

    # Khởi tạo bộ phát hiện đối tượng trên frame
    obj.init(frame)

    # Nhận dạng và vẽ đối tượng trên frame
    img = obj.drawObj("cat")

    # Hiển thị kết quả
    cv2.imshow("Kết quả", img)

    # Kiểm tra phím nhấn để thoát
    key = cv2.waitKey(1)
    if key == 27:  # Phím Esc
        break

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
