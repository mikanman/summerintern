import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from cut import Max_Min, Make_Dice
from image_manage import Image_mane, WordChanger
from model import Media, My_model

def main():

  image = Image_mane()
  media = Media()
  word_ch = WordChanger()
  model = My_model()

  while True:

    image.update()
  
    x_mize = Max_Min(image.width)
    y_mize = Max_Min(image.height)

    media.result(image.img)
    if media.landmarks is None:
      cv2.imshow("Frame", image.image)


      key = cv2.waitKey(1)

      if key == 27:
        break
      continue


    for i in range(21):
      x = media.landmarks[0].landmark[i].x * image.width
      y = media.landmarks[0].landmark[i].y * image.height

      x_mize.update(x)
      y_mize.update(y)
    
    make = Make_Dice(x_mize, y_mize)
    make.update()

    image.drow_line(make)

    model.act(image.img, make)

    word_ch.text_out(image.image, model.word, model.prop )

    cv2.imshow("Frame",np.array(word_ch.img_pil))

    key = cv2.waitKey(1)

    if key == 27:
      break

  image.clear()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()