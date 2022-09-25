import tensorflow as tf
import numpy as np
import cv2


label=np.array(['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん'])



new_model = tf.keras.models.load_model('model/my_model.h5')


img = cv2.cvtColor(cv2.imread('IMG_1823.jpg'), cv2.COLOR_BGR2RGB)

img = cv2.resize(img, dsize=(256, 256))/ 255.0


img_expand = img[np.newaxis, ...]



predictions_single = new_model.predict(img_expand)

predictions_single = predictions_single[0]

a = np.argpartition(-predictions_single, 5)[:5]

print(label[a])

print(img_expand.shape)
