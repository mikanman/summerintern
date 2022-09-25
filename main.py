import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf

import cut

cap = cv2.VideoCapture(0)

# 初期設定
hands = mp.solutions.hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
    )

label=np.array(['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん'])

model = tf.keras.models.load_model('model/my_model.h5')

while True:

  ret, image = cap.read()

  img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  img_size = cv2.resize(img, dsize=(256, 256))/ 255.0
  img_expand = img_size[np.newaxis, ...]

  predictions_single = model.predict(img_expand)
  predictions_single = predictions_single[0]
  answer = np.argpartition(-predictions_single, 5)[:5]

  results = hands.process(img)
  
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
  print(label[answer])
  # cv2.putText(image,
  #             text='sample text',
  #             org=(100, 300),
  #             fontFace=cv2.FONT_HERSHEY_SIMPLEX,
  #             fontScale=1.0,
  #             color=(0, 255, 0),
  #             thickness=2,
  #             lineType=cv2.LINE_4)

  cv2.imshow("Frame", image)

  key = cv2.waitKey(1)

  if key == 27:
    break

cap.release()
cv2.destroyAllWindows()