import cv2
"""
img = cv2.imread("images.jpg")
img = cv2.resize(img, (512, 512))
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


cv2.imshow("BGR", img)

cv2.imshow("RGB", img_gris)
cv2.waitKey(0)
"""

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # code here
    face_dectector = cv2.CascadeClassifier("haarcascade_features.xml")
    eyes_detector = cv2.CascadeClassifier("eyes_features.xml")
    faces = face_dectector.detectMultiScale(gray, 1.3, 5)
    eyes = eyes_dectector.detectMultiScale(gray, 1.3, 5)

    for face in faces:
        (x, y, w, h) = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # ===========

    cv2.imshow("My video", frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()