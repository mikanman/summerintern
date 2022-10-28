import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np


class Image_mane():

    def __init__(self):
        self.cap = cv2.VideoCapture(1)

    def update(self):
        ret, self.image = self.cap.read()
        self.height, self.width, _ = self.image.shape

        self.img = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)

    def drow_line(self, make):
        self.image = cv2.line(
            self.image,
            (make.x_min,make.y_min),
            (make.x_min,make.y_max),
            (0,0,255),
            3
        )

        self.image = cv2.line(
            self.image,
            (make.x_max,make.y_min),
            (make.x_max,make.y_max),
            (0,0,255),
            3
        )

        self.image = cv2.line(
            self.image,
            (make.x_min,make.y_min),
            (make.x_max,make.y_min),
            (0,0,255),
            3
        )

        self.image = cv2.line(
            self.image,
            (make.x_min,make.y_max),
            (make.x_max,make.y_max),
            (0,0,255),
            3
        )

    def resize(self, make):
        img_size = cv2.resize(self.img[make.y_min : make.y_max, make.x_min: make.x_max],
        dsize=(256, 256))/ 255.0
        self.img_expand = img_size[np.newaxis, ...]


    def clear(self):
        self.cap.release()



class WordChanger():

    def __init__(self):
        #初期設定
        self.fill = (10,10,10,0) #B(青)・G(緑)・R(赤)・A(透明度)
        fontpath ='C:\Windows\Fonts\HGRPP1.TTC' 
        self.font = ImageFont.truetype(fontpath, 32) # フォントサイズが32
        self.position_w = (0,0) 
        self.position_p = (50,0) 


    def text_out(self, image, word, prop):
        self.img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(self.img_pil)# drawインスタンスを生成
        draw.text(self.position_w, word, font = self.font , fill = self.fill )
        draw.text(self.position_p, prop, font = self.font , fill = self.fill )
    
