import cv2

cap = cv2.VideoCapture(0)  # 通常預設 0
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)  # 1024, 800, 640, 320
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)  # 768, 600, 480, 240

# 人臉特徵檔
face_Cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')
# 眼睛特徵檔
eyes_Cascade = cv2.CascadeClassifier('./xml/haarcascade_eye.xml')


while True:
    ret, frame = cap.read()
    if (ret == True):
        print(ret, frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # face 的座標範圍
        faces = face_Cascade.detectMultiScale(
            gray,  # 待檢測圖片
            scaleFactor=1.1,  # 檢測粒度(越小越精準(速度慢)；越大越模糊(速度快))
            minNeighbors=5,  # 每個目標至少檢測到幾次成功，才被認定是 face
            minSize=(30, 30),  # 設定數據最小搜尋的尺寸
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # 在 face 周圍畫上矩形框
        for (x, y, w, h) in faces:  # (B  G   R),  2: 線框寬度
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 偵測眼睛
        roi_gray = gray[y:y + h, x:x + w]  # 人臉區域(灰階)
        roi_color = frame[y:y + h, x:x + w]  # 人臉區域(彩色)
        eyes = eyes_Cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(10, 10),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    # ----------------------------------------------------------------------------
    # 顯示影像
    cv2.imshow('Michelle', frame)
    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
