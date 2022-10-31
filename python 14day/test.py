import os
from PIL import Image
from keras.preprocessing import image
import numpy as np
import keras

# print(len(os.listdir('./cats_and_dogs/train/dogs')))
# print(len(os.listdir('./cats_and_dogs/train/cats')))
#25000

# print(len(os.listdir('./cats_and_dogs/validation/dogs')))
# print(len(os.listdir('./cats_and_dogs/validation/cats')))
#660
model = keras.models.load_model('dog_cat.h5')

img = Image.open('./cats_and_dogs/test/random/cat.6.jpg','r')
img = img.resize((64,64))
array = image.img_to_array(img)
array = np.expand_dims(img,axis=0)

result = model.predict([[array]])
print(result)


