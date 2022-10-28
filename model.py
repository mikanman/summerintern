import mediapipe as mp
import numpy as np
import tensorflow as tf
import cv2

class Media():

    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=True,
            max_num_hands=1,
            min_detection_confidence=0.5
            )

    def result(self, img):
        self.results = self.hands.process(img)
        self.landmarks = self.results.multi_hand_landmarks
  


class My_model():

    def __init__(self):
        self.label = np.array(['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん'])
        self.model = tf.keras.models.load_model('model/my_model.h5')


    def pre_make(self, img, make):
        img_size = cv2.resize(img[make.y_min : make.y_max, make.x_min: make.x_max],
        dsize=(256, 256))/ 255.0
        self.img_expand = img_size[np.newaxis, ...]


    def predict(self):
        predictions_single = self.model.predict(self.img_expand)
        print(predictions_single)
        self.predictions_single = predictions_single[0]
        self.answer = np.argpartition(-self.predictions_single, 5)[:5]


    def output(self):
        ans_list = self.label[self.answer]
        # print(ans_list)
        self.word = '\n'.join(ans_list)
        self.prop =''

        x_list = self.predictions_single[self.answer].tolist()
        for x in x_list:
           self.prop += str(round(x*100, 2)).zfill(5) +'%\n'

    def act(self, img, make):
        self.pre_make(img, make)
        self.predict()
        self.output()
        