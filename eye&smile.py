import cv2
import mediapipe as mp
import warnings

warnings.filterwarnings('ignore')

mp_face = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
face_det = mp_face.FaceDetection(min_detection_confidence = 1, model_selection = 0)

cao = cv2.VideoCapture(0)

while cao.isOpened():
    r, f = cao.read()

    if r == True:
        f = cv2.flip(f, 1)
        f = cv2.resize(f, (500, 500))
        f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
        res = face_det.process(f)
        f = cv2.cvtColor(f, cv2.COLOR_RGB2BGR)

        if res.detections:
            for cr in res.detections:
                mp_draw.draw_detection(f, cr)

        cv2.imshow('detected', f)

        if cv2.waitKey(20) & 0xFF == ord('p'):
            break
    else:
        break

cao.release()
cv2.destroyAllWindows()

