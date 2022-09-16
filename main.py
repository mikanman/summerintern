import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

import tensorflow as tf

import cut

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
    )

# new_model = tf.keras.models.load_model('saved_model')


while True:

  ret, image = cap.read()

  results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  
  image_height, image_width, _ = image.shape


  x_mize = cut.Max_Min(image_width)
  y_mize = cut.Max_Min(image_height)

  hand_landmarks = results.multi_hand_landmarks
  if not results.multi_hand_landmarks:
    cv2.imshow("Frame", image)

    key = cv2.waitKey(1)

    if key == 27:
      break
    continue

  for i in range(21):
    x = hand_landmarks[0].landmark[i].x * image_width
    y = hand_landmarks[0].landmark[i].y * image_height

    x_mize.update(x)
    y_mize.update(y)

  make = cut.Make_Dice(x_mize, y_mize)
  make.update()

  image = cv2.line(
    image,
    (make.x_min,make.y_min),
    (make.x_min,make.y_max),
    (0,0,255),
    3
  )
  image = cv2.line(
    image,
    (make.x_max,make.y_min),
    (make.x_max,make.y_max),
    (0,0,255),
    3
  )
  image = cv2.line(
    image,
    (make.x_min,make.y_min),
    (make.x_max,make.y_min),
    (0,0,255),
    3
  )
  image = cv2.line(
    image,
    (make.x_min,make.y_max),
    (make.x_max,make.y_max),
    (0,0,255),
    3
  )

  cv2.imshow("Frame", image)

  key = cv2.waitKey(1)

  if key == 27:
    break

cap.release()
cv2.destroyAllWindows()