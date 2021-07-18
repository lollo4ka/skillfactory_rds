import pandas as pd
import os
import warnings
import zipfile

import tensorflow
from tensorflow.python.debug.examples.v1.debug_keras import tf
from tensorflow.python.framework.ops import disable_eager_execution
disable_eager_execution()

import efficientnet.keras as efn
import pandas as pd
from keras import optimizers
from keras.callbacks import ModelCheckpoint
from keras.layers import *
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.applications.xception import Xception

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

#увеличим дефолтный размер графиков
# from pylab import rcParams
# rcParams['figure.figsize'] = 10, 5
# #графики в svg выглядят более четкими
# %config InlineBackend.figure_format = 'svg'
# %matplotlib inline

# print(os.listdir("../input"))

# В сетап выношу основные настройки, так удобней их перебирать в дальнейшем

EPOCHS               = 5  # эпох на обучение
BATCH_SIZE           = 64 # уменьшаем batch если сеть большая, иначе не поместится в память на GPU
LR                   = 1e-4
VAL_SPLIT            = 0.15 # сколько данных выделяем на тест = 15%

CLASS_NUM            = 10
IMG_SIZE             = 224
IMG_CHANNELS         = 3
input_shape          = (IMG_SIZE, IMG_SIZE, IMG_CHANNELS)

RANDOM_SEED = 42

DATA_PATH = '/Users/alina/Code/skillfactory/юнит_6/юнит_9/sf/data/'
PATH = "/Users/alina/Code/skillfactory/юнит_6/юнит_9/sf/data/car/"

# загружаем данные
train_df = pd.read_csv(DATA_PATH+"train.csv")
sample_submission = pd.read_csv(DATA_PATH+"sample-submission.csv")

# распаковываем картинки
# print('Распаковываем картинки')
# # Will unzip the files so that you can see them..
# for data_zip in ['train.zip', 'test.zip']:
#     with zipfile.ZipFile(DATA_PATH + data_zip, "r") as z:
#         z.extractall(PATH)
#
# print(os.listdir(PATH))

# Первая аугментация данных, пробная

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range = 5,
    width_shift_range=0.1,
    height_shift_range=0.1,
    validation_split=0.1, # set validation split
    horizontal_flip=False)

test_datagen = ImageDataGenerator(rescale=1. / 255)

# "Заворачиваем" наши данные в generator

train_generator = train_datagen.flow_from_directory(
    PATH +'train/',
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=True, seed=RANDOM_SEED,
    subset='training') # set as training data

test_generator = train_datagen.flow_from_directory(
    PATH +'train/',
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=True, seed=RANDOM_SEED,
    subset='validation') # set as validation data

# test_sub_generator = test_datagen.flow_from_dataframe(
#     dataframe=sample_submission,
#     directory=PATH +'test_upload',
#     x_col="Id",
#     y_col=None,
#     shuffle=False,
#     class_mode=None,
#     seed=RANDOM_SEED,
#     target_size=(IMG_SIZE, IMG_SIZE),
#     batch_size=BATCH_SIZE,)

# base_model = Xception(weights='imagenet', include_top=False, input_shape = input_shape)
# использую EfficientNetB0 она в топе и тратит меньше ресурсов по сравнению с другими моделями
base_model = efn.EfficientNetB0(weights='imagenet', include_top=False, input_shape= input_shape)

# Устанавливаем новую "голову"
# Тут тоже можно поиграться, попробуй добавить Batch Normalization например.

x = base_model.output
x = GlobalAveragePooling2D()(x)
# let's add a fully-connected layer
x = Dense(256, activation='relu')(x)
x = Dropout(0.25)(x)
# and a logistic layer -- let's say we have 10 classes
predictions = Dense(CLASS_NUM, activation='softmax')(x)

# this is the model we will train
model = Model(inputs=base_model.input, outputs=predictions)
model.compile(loss="categorical_crossentropy", optimizer=optimizers.Adam(lr=LR), metrics=["accuracy"])

checkpoint = ModelCheckpoint('best_model.hdf5' , monitor = ['val_acc'] , verbose = 1  , mode = 'max')
callbacks_list = [checkpoint]

tf.compat.v1.experimental.output_all_intermediates(True)
# Обучаем
history = model.fit_generator(
        train_generator,
        steps_per_epoch = len(train_generator),
        validation_data = test_generator,
        validation_steps = len(test_generator),
        epochs = EPOCHS
        # callbacks = callbacks_list
)

model.save('../working/model_last.hdf5')
model.load_weights('best_model.hdf5')

scores = model.evaluate_generator(test_generator, steps=len(test_generator), verbose=1)
print("Accuracy: %.2f%%" % (scores[1]*100))




# # Загружаем данные из датасета
# X, y = fetch_california_housing(return_X_y=True, as_frame=True)
#
# # добавляем поле "obj_id" чтобы в дальнейшем идентифицировать объект
# X['obj_id'] = list(range(X.shape[0]))
#
# # Разбиваем датасет на трейн и тест по заданным параметрам: размера теста и random_state
# TEST_SIZE = 0.2
# RANDOM_STATE = 7
#
# X_train, X_test, y_train, y_test = train_test_split(X, y,
#                                                     test_size=TEST_SIZE,
#                                                     random_state=RANDOM_STATE)
# print('Data shapes:', X_train.shape, X_test.shape, y_train.shape, y_test.shape)
#
# # Обучаем модель LinearRegression из sklearn на трейне
# # при этом не забываем удалить из трейна колонку obj_id
# model = LinearRegression()
# model.fit(X_train.drop(columns=['obj_id']), y_train)
#
# # Делаем предикт на тесте (не забываем удалить колонку obj_id)
# # и измеряем ошибку по MSE
# y_pred = model.predict(X_test.drop(columns=['obj_id']))
# print('MSE on test:', round(mean_squared_error(y_test, y_pred), 6))

# # Сериализуем обученную модель с помощью pickle в файл "webinar_model.pkl"
# # в папку "src" рядом
# MODEL_FILE = '_webinar_model.pkl'
# FEATURE_ORDER_FILE = '_feature_order.pkl'
# TEST_DATA_FILE = '_test_data.pkl'
#
#
# # ******** НИЖЕ НАПИШИТЕ КОД СЕРИАЛИЗАЦИИ МОДЕЛИ В ФАЙЛ MODEL_FILE
# # ........
# with open(MODEL_FILE, 'wb') as output:
#     pickle.dump(model, output)
#
#
# # Тестовую часть датасета сериализуем с помощью pickle для использования в дальнейшем
# # Формат сохранения тестовых данных - Pandas DataFrame
# # (по желанию можно использовать любую другую конструкцию
# # python list/dict, numpy array и т.п., учитывая что
# # потом из тестовых данных нужно будет доставать признаки)
#
#
# # ******** НИЖЕ НАПИШИТЕ КОД СЕРИАЛИЗАЦИИ ТЕСТОВЫХ ДАННЫХ В ФАЙЛ TEST_DATA_FILE
# # в идеале сохранять в отдельную базу данных
# with open(TEST_DATA_FILE, 'wb') as output:
#     pickle.dump(X_test, output)
#
#
# # Сохраним в отдельный файл feature_order - порядок названий признаков в нашем датасете
# feature_order = X.columns.tolist()
# feature_order.remove('obj_id')
# print('Feature order:', feature_order)
#
#
# # ******** НИЖЕ НАПИШИТЕ КОД СЕРИАЛИЗАЦИИ feature_order В ФАЙЛ FEATURE_ORDER_FILE
# # ........
# with open(FEATURE_ORDER_FILE, 'wb') as output:
#     pickle.dump(feature_order, output)