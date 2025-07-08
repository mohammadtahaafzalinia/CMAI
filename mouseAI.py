import cv2
import mediapipe as mp
import pyautogui
import math

# ---------- settings ----------
pyautogui.FAILSAFE = False
pyautogui.PAUSE    = 0
screen_w, screen_h = pyautogui.size()

hands = mp.solutions.hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH , 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS         , 30)

alpha = 0.25
smooth_x, smooth_y = pyautogui.position()

# status clicks
is_left_clicked = False
is_right_clicked = False

while True:
    ret, img = cap.read()
    if not ret: break
    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    if res.multi_hand_landmarks:
        lm = res.multi_hand_landmarks[0].landmark
        i_tip = lm[8]   # index
        t_tip = lm[4]   # thumb
        m_tip = lm[12]  # middle

        # page coordinates
        x, y = int(i_tip.x * screen_w), int(i_tip.y * screen_h)
        smooth_x += alpha * (x - smooth_x)
        smooth_y += alpha * (y - smooth_y)
        pyautogui.moveTo(int(smooth_x), int(smooth_y))

        # distances
        dist_index_thumb = math.hypot(i_tip.x - t_tip.x, i_tip.y - t_tip.y)
        dist_middle_thumb = math.hypot(m_tip.x - t_tip.x, m_tip.y - t_tip.y)

        # left click (index + thumb)
        if dist_index_thumb < 0.06:
            if not is_left_clicked:
                pyautogui.click()
                is_left_clicked = True
                print("🖱 Left Click")
        else:
            is_left_clicked = False  # Fingers apart → ready for another click

        # right click (middle + thumb)
        if dist_middle_thumb < 0.05:
            if not is_right_clicked:
                pyautogui.click(button='right')
                is_right_clicked = True
                print("🖱 Right Click")
        else:
            is_right_clicked = False

    cv2.imshow("Hand Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()