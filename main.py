import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(max_num_hands=1)

cam = cv2.VideoCapture(0)  # 0th is the default camera of the device
cordss = {}

current_gesture = None
previous_gesture = None
gesture_start_time = 0  # Time when the gesture was first detected
gesture_hold_time = 0.5  # Minimum time to hold a gesture before printing

while True:
    _, image = cam.read()
    image = cv2.flip(image, 1)  # Flip the image horizontally
    results = hands.process(image)
    # image=cv2.cvtColor(image,cv2,COLOR_RGB2GRAY) # Uncomment if grayscale conversion is needed
    height, width, _ = image.shape  # Height, width, and channel -> channel is RGB

    if results.multi_hand_landmarks:
        for handid, hand_landmarks in enumerate(results.multi_hand_landmarks):  # For each detected hand
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
            for id, lms in enumerate(hand_landmarks.landmark):  # Each landmark inside hand
                # if id == 8:
                #      print(lms.y)

                x_cord = lms.x * width
                y_cord = lms.y * height
                cordss[id] = (x_cord, y_cord)

                # if id == 4:
                #      print("4  ",lms.x)
                # if id == 3:
                #      print("1  ",lms.x)

            try:
                detected_gesture = None

                # Scissors gesture
                if cordss[8][1] < cordss[5][1] and cordss[12][1] < cordss[9][1] and cordss[16][1] > cordss[13][1] and cordss[20][1] > cordss[17][1]:
                    detected_gesture = "Scissors"
                # Rock gesture
                elif cordss[8][1] > cordss[5][1] and cordss[12][1] > cordss[9][1] and cordss[16][1] > cordss[13][1] and cordss[20][1] > cordss[17][1] and cordss[4][0] > cordss[3][0]:
                    detected_gesture = "Rock"
                # Paper gesture
                elif cordss[8][1] < cordss[5][1] and cordss[12][1] < cordss[9][1] and cordss[16][1] < cordss[13][1] and cordss[20][1] < cordss[17][1] and cordss[4][0] < cordss[3][0]:
                    detected_gesture = "Paper"

                # Method 2: Avoid repetition using gesture persistence check
                if detected_gesture == current_gesture:
                    if time.time() - gesture_start_time > gesture_hold_time and detected_gesture != previous_gesture:
                        print("\n", detected_gesture, "\n")
                        previous_gesture = detected_gesture
                else:
                    current_gesture = detected_gesture
                    gesture_start_time = time.time()

                # Method 1: Normal (without persistence check)
                # if cordss[8][1] < cordss[5][1] and cordss[12][1] < cordss[9][1] and cordss[16][1] > cordss[13][1] and cordss[20][1] > cordss[17][1]:
                #     print("Scissors")
                # if cordss[8][1] > cordss[5][1] and cordss[12][1] > cordss[9][1] and cordss[16][1] > cordss[13][1] and cordss[20][1] > cordss[17][1] and cordss[4][0] > cordss[3][0]:
                #     print("Rock")
                # if cordss[8][1] < cordss[5][1] and cordss[12][1] < cordss[9][1] and cordss[16][1] < cordss[13][1] and cordss[20][1] < cordss[17][1] and cordss[4][0] < cordss[3][0]:
                #     print("Paper")
            except KeyError:
                pass

    # image=image[100:200,200:300]={255,0,255}  # Uncomment if specific cropping or color adjustment is needed
    cv2.imshow("Project", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cam.release()
cv2.destroyAllWindows()
