import os
from math import sqrt

import matplotlib
from tensorflow import keras
from tensorflow.keras.models import Model

from keras.models import Model

from tensorflow.keras.applications import EfficientNetB7

import matplotlib.pyplot as plt

from PIL import Image
import numpy as np

results=[]
# matplotlib.use('TkAgg')
def proprecess_image(img_path):
    image = Image.open(img_path)
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, 0)
    return image

def get_model(model, output_layers):
    show_model = Model(inputs=model.inputs, outputs=output_layers.output)
    return show_model
def get_model_by_layers(model, layer_id, weights_path):
    layers_dict = {}
    for index, layer in enumerate(model.layers):
        # print(index,":",layer.name)
        layers_dict[index] = layer.name

    def generate_model(model, layer_id, weights_path):
        func_layer = model.get_layer(name=layers_dict[layer_id])
        new_model = get_model(model, func_layer)
        new_model.load_weights(weights_path, by_name=True)

        return new_model

    conv_model = generate_model(model, layer_id, weights_path)
    return conv_model

def visualize_model_output(model, image_path, layer_id, weights_path, num_filter,cnt):
    image = proprecess_image(image_path)
    output_model = get_model_by_layers(model, layer_id, weights_path)
    # print("======output model summary ======")
    # print("ans:",output_model)
    result = output_model.predict(image)

    for i in range(num_filter):
        plt.subplot(2, 2, i+1)
        plt.imshow(result[0, :, :, i])
    upload_path = os.path.join('static/uploads_ft', str(cnt))
    results.append(upload_path+".png")
    plt.savefig(upload_path)
    plt.show()



def func(img_url,weight_url,filter_num):
    results=[]
    inception_model = EfficientNetB7(include_top=True, weights=None, input_shape=(224, 224, 3), classes=4)




    # image_path = r"C:\Users\ROG\Desktop\maize_leaf\Cercospora_leaf_spot Gray_leaf_spot\0b5492ee-253d-4a13-ad5a-780cb954b09a___RS_GLSp 4615 copy.jpg"
    image_path = img_url
    # weights_path = r"C:\Users\ROG\机器学习\GoogLeNet\EfficientNet+多任务+微调(玉米)（不错）.h5"
    weights_path = weight_url

    conv_layers_id = [15,227,812]
    num_filter=filter_num
    cnt=0
    for layer_id in conv_layers_id:
        visualize_model_output(inception_model, image_path, layer_id, weights_path, num_filter,cnt)
        cnt+=1
    for i in results:
        print(i)
    return results

# image_path = r"C:\Users\ROG\Desktop\maize_leaf\Cercospora_leaf_spot Gray_leaf_spot\0b5492ee-253d-4a13-ad5a-780cb954b09a___RS_GLSp 4615 copy.jpg"
# weights_path = r"C:\Users\ROG\机器学习\GoogLeNet\EfficientNet+多任务+微调(玉米)（不错）.h5"
# func(img_url=image_path,weight_url=weights_path,filter_num=4)
# for i in results:
#     print(i)