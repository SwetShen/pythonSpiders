import keras
import os
from keras.preprocessing.image import ImageDataGenerator

#加载训练好的模型
model = keras.models.load_model('dog_cat.h5')



base_dir = './cats_and_dogs/'
#测试图集'./cats_and_dogs/test'
test_dir = os.path.join(base_dir,'test')



#全部都是狗的图片的合集
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(64,64),
    batch_size=10,
    class_mode=None
)

print(test_generator)

#使用模型预测
#sigmod 0(猫) ~ 1(狗)
result = model.predict(test_generator)

n = 0
#遍历图片名称
for fname in os.listdir(os.path.join(test_dir,'random')):
    print(fname,list(result.reshape(-1))[n])
    n += 1

from keras.preprocessing import image
