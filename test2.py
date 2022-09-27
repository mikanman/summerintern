import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
  ret, frame = cap.read()
  # 表示する色
  b,g,r,a = 0,255,0,0 #B(青)・G(緑)・R(赤)・A(透明度)
  # 表示させる文字
  message = 'OpenCV(オープンシーブイ)'
  fontpath ='C:\Windows\Fonts\HGRPP1.TTC' 
  font = ImageFont.truetype(fontpath, 32) # フォントサイズが32
  img_pil = Image.fromarray(frame)# 配列の各値を8bit(1byte)整数型(0～255)をPIL Imageに変換。
  draw = ImageDraw.Draw(img_pil)# drawインスタンスを生成
  position = (10,80) # テキスト表示位置
  draw.text(position, message, font = font , fill = (b, g, r, a) )# drawにテキストを記載 fill:色 BGRA (RGB)

  cv2.imshow("frame",np.array(img_pil))

  # qキーが押されたら途中終了
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break