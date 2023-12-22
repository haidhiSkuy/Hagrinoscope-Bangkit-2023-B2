from PIL import Image
import numpy as np
import tensorflow as tf

fruit_model = tf.keras.models.load_model('ml_model/buah.h5')
soil_model = tf.keras.models.load_model('ml_model/soil.h5')

fruit_label = {
    0: 'ripe_banana', 1: 'unripe_banana', 2: 'half_ripe_papaya',
    3: 'ripe_papaya', 4: 'unripe_papaya', 5: 'half_ripe_pineapple',
    6: 'ripe_pineapple', 7: 'half_ripe_tomato', 8: 'ripe_tomato',
    9: 'unripe_tomato'
}

soil_label = {
    0: 'black_soil', 1: 'cinder_soil', 2: 'laterite_soil', 3: 'peat_soil', 4: 'yellow_soil'
}


def fruit_predict(image):
    image_resized = image.resize((160, 160))
    image_array = np.array(image_resized) / 255.0

    if len(image_array.shape) > 2:
        image_array = image_array[..., :3]

    image_array = np.expand_dims(image_array, axis=0)
    predictions = fruit_model.predict(image_array)
    predicted_class = np.argmax(predictions, axis=1)
    prediction_label = fruit_label[predicted_class[0]]
    return prediction_label


def soil_predict(image):
    image_resized = image.resize((160, 160))
    image_array = np.array(image_resized) / 255.0

    if image_array.shape[2] == 4:
        image_array = image_array[..., :3]

    image_array = np.expand_dims(image_array, axis=0)
    predictions = soil_model.predict(image_array, verbose=0)
    predicted_class = np.argmax(predictions, axis=1)
    prediction_label = soil_label[predicted_class[0]]
    return prediction_label
