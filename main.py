import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import ImageFont, ImageDraw, Image

import cut

cap = cv2.VideoCapture(0)

# 初期設定
hands = mp.solutions.hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
    )

label=np.array(['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん'])

b,g,r,a = 10,10,10,0 #B(青)・G(緑)・R(赤)・A(透明度)
fontpath ='C:\Windows\Fonts\HGRPP1.TTC' 
font = ImageFont.truetype(fontpath, 32) # フォントサイズが32
position_w = (0,0) 
position_p = (50,0) 


model = tf.keras.models.load_model('model/my_model.h5')

while True:

  ret, image = cap.read()

  img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

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

  
  img_size = cv2.resize(img[make.y_min : make.y_max, make.x_min: make.x_max],
   dsize=(256, 256))/ 255.0
  img_expand = img_size[np.newaxis, ...]

  predictions_single = model.predict(img_expand)
  predictions_single = predictions_single[0]
  answer = np.argpartition(-predictions_single, 5)[:5]

  word = '\n'.join(label[answer])
  prop =''
  x_list = predictions_single[answer].tolist()
  for x in x_list:
    prop += str(round(x*100, 2)).zfill(5) +'%\n'

  img_pil = Image.fromarray(image)
  draw = ImageDraw.Draw(img_pil)# drawインスタンスを生成
  draw.text(position_w, word, font = font , fill = (b, g, r, a) )
  draw.text(position_p, prop, font = font , fill = (b, g, r, a) )

  cv2.imshow("Frame",np.array(img_pil))

  key = cv2.waitKey(1)

  if key == 27:
    break

cap.release()
cv2.destroyAllWindows()