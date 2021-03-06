import numpy as np
from random import shuffle
# from preprocessor import preprocess_input
# from preprocessor import _imread as imread
# from preprocessor import _imresize as imresize
# from preprocessor import to_categorical
import scipy.ndimage as ndi
import cv2
import os
from scipy.misc import imread, imresize

def preprocess_input(x, v2=True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x

def _imread(image_name):
        return imread(image_name)

def _imresize(image_array, size):
        return imresize(image_array, size)

def to_categorical(integer_classes, num_classes=2):
    integer_classes = np.asarray(integer_classes, dtype='int')
    num_samples = integer_classes.shape[0]
    categorical = np.zeros((num_samples, num_classes))
    categorical[np.arange(num_samples), integer_classes] = 1
    return categorical

detect_face_path = '/home/yanhong/Downloads/next_step/Xception/trained_models/detection_models/haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(detect_face_path)
def crop_face(img,face_cascade):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #will display another window with same vedio feed but grey in color .You can always use different                   
    faces=face_cascade.detectMultiScale(gray,1.3,3)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)                
        roi_gray = gray[x:x+w,y:y+h]
        roi_color = img[x:x+w,y:y+h]
        crop_img = img[y:y+h, x:x+w]
    return(crop_img)

class ImageGenerator(object):
    def __init__(self, ground_truth_data, batch_size, image_size,
                train_keys, validation_keys,
                ground_truth_transformer=None,
                path_prefix=None,
                saturation_var=0.5,
                brightness_var=0.5,
                contrast_var=0.5,
                lighting_std=0.5,
                horizontal_flip_probability=0.5,
                vertical_flip_probability=0.5,
                do_random_crop=False,
                grayscale=False,
                zoom_range=[0.75, 1.25],
                translation_factor=.3):

        self.ground_truth_data = ground_truth_data
        self.ground_truth_transformer = ground_truth_transformer
        self.batch_size = batch_size
        self.path_prefix = path_prefix
        self.train_keys = train_keys
        self.validation_keys = validation_keys
        self.image_size = image_size
        self.grayscale = grayscale
        self.color_jitter = []
        if saturation_var:
            self.saturation_var = saturation_var
            self.color_jitter.append(self.saturation)
        if brightness_var:
            self.brightness_var = brightness_var
            self.color_jitter.append(self.brightness)
        if contrast_var:
            self.contrast_var = contrast_var
            self.color_jitter.append(self.contrast)
        self.lighting_std = lighting_std
        self.horizontal_flip_probability = horizontal_flip_probability
        self.vertical_flip_probability = vertical_flip_probability
        self.do_random_crop = do_random_crop
        self.zoom_range = zoom_range
        self.translation_factor = translation_factor

    def _do_random_crop(self, image_array):
        height = image_array.shape[0]
        width = image_array.shape[1]
        x_offset = np.random.uniform(0, self.translation_factor * width)
        y_offset = np.random.uniform(0, self.translation_factor * height)
        offset = np.array([x_offset, y_offset])
        scale_factor = np.random.uniform(self.zoom_range[0],
                                        self.zoom_range[1])
        crop_matrix = np.array([[scale_factor, 0],
                                [0, scale_factor]])
        image_array = np.rollaxis(image_array, axis=-1, start=0)
        image_channel = [ndi.interpolation.affine_transform(image_channel,
                        crop_matrix, offset=offset, order=0, mode='nearest',
                        cval=0.0) for image_channel in image_array]
        image_array = np.stack(image_channel, axis=0)
        image_array = np.rollaxis(image_array, 0, 3)
        return image_array

    def do_random_rotation(self, image_array):
        height = image_array.shape[0]
        width = image_array.shape[1]
        x_offset = np.random.uniform(0, self.translation_factor * width)
        y_offset = np.random.uniform(0, self.translation_factor * height)
        offset = np.array([x_offset, y_offset])
        scale_factor = np.random.uniform(self.zoom_range[0],
                                        self.zoom_range[1])
        crop_matrix = np.array([[scale_factor, 0],
                                [0, scale_factor]])
        image_array = np.rollaxis(image_array, axis=-1, start=0)
        image_channel = [ndi.interpolation.affine_transform(image_channel,
                        crop_matrix, offset=offset, order=0, mode='nearest',
                        cval=0.0) for image_channel in image_array]
        image_array = np.stack(image_channel, axis=0)
        image_array = np.rollaxis(image_array, 0, 3)
        return image_array

    def _gray_scale(self, image_array):
        return image_array.dot([0.299, 0.587, 0.114])

    def saturation(self, image_array):
        gray_scale = self._gray_scale(image_array)
        alpha = 2.0 * np.random.random() * self.brightness_var
        alpha = alpha + 1 - self.saturation_var
        image_array = alpha * image_array + (1 - alpha) * gray_scale[:, :, None]
        return np.clip(image_array, 0, 255)

    def brightness(self, image_array):
        alpha = 2 * np.random.random() * self.brightness_var
        alpha = alpha + 1 - self.saturation_var
        image_array = alpha * image_array
        return np.clip(image_array, 0, 255)

    def contrast(self, image_array):
        gray_scale = (self._gray_scale(image_array).mean() *
                        np.ones_like(image_array))
        alpha = 2 * np.random.random() * self.contrast_var
        alpha = alpha + 1 - self.contrast_var
        image_array = image_array * alpha + (1 - alpha) * gray_scale
        return np.clip(image_array, 0, 255)

    def lighting(self, image_array):
        covariance_matrix = np.cov(image_array.reshape(-1,3) /
                                    255.0, rowvar=False)
        eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)
        noise = np.random.randn(3) * self.lighting_std
        noise = eigen_vectors.dot(eigen_values * noise) * 255
        image_array = image_array + noise
        return np.clip(image_array, 0 ,255)

    def horizontal_flip(self, image_array, box_corners=None):
        if np.random.random() < self.horizontal_flip_probability:
            image_array = image_array[:, ::-1]
            if box_corners != None:
                box_corners[:, [0, 2]] = 1 - box_corners[:, [2, 0]]
        return image_array, box_corners

    def vertical_flip(self, image_array, box_corners=None):
        if (np.random.random() < self.vertical_flip_probability):
            image_array = image_array[::-1]
            if box_corners != None:
                box_corners[:, [1, 3]] = 1 - box_corners[:, [3, 1]]
        return image_array, box_corners

    def transform(self, image_array, box_corners=None):
        shuffle(self.color_jitter)
        for jitter in self.color_jitter:
            image_array = jitter(image_array)
        if self.lighting_std:
            image_array = self.lighting(image_array)
        if self.horizontal_flip_probability > 0:
            image_array, box_corners = self.horizontal_flip(image_array,
                                                            box_corners)
        if self.vertical_flip_probability > 0:
            image_array, box_corners = self.vertical_flip(image_array,
                                                            box_corners)
        return image_array, box_corners

    def preprocess_images(self, image_array):
        return preprocess_input(image_array)

    def flow(self, mode='train'):
            while True:
                if mode =='train':
                    shuffle(self.train_keys)
                    keys = self.train_keys
                elif mode == 'val' or  mode == 'demo':
                    shuffle(self.validation_keys)
                    keys = self.validation_keys
                else:
                    raise Exception('invalid mode: %s' % mode)
                inputs = []
                targets = []
                targets_1 = []
                targets_2 = []
                for key in keys:
                    image_path = self.path_prefix + key
                    #print image_path
                    if not os.path.exists(image_path):
                        continue
                    image_array = imread(image_path)
                    image_array = imresize(image_array, self.image_size)
                    num_image_channels = len(image_array.shape)
                    if num_image_channels != 3:
                        continue
                    ground_truth = self.ground_truth_data[key]
                    if ground_truth[1] > 100 or ground_truth[1] < 0:
                        continue
                    if self.do_random_crop:
                        image_array = self._do_random_crop(image_array)
                    image_array = image_array.astype('float32')
                    if mode == 'train' or mode == 'demo':
                        if self.ground_truth_transformer != None:
                            image_array, ground_truth = self.transform(
                                                                image_array,
                                                                ground_truth)
                            ground_truth = (
                                self.ground_truth_transformer.assign_boxes(
                                                            ground_truth))
                        else:
                            image_array = self.transform(image_array)[0]

                    if self.grayscale:
                        image_array = cv2.cvtColor(image_array.astype('uint8'),
                                        cv2.COLOR_RGB2GRAY).astype('float32')
                        image_array = np.expand_dims(image_array, -1)


                    inputs.append(image_array)
                    #print ground_truth
                    targets_1.append(ground_truth[0])
                    targets_2.append(ground_truth[1])
                    #print targets_1,targets_2
                    #targets.append(ground_truth)
                    #print key
                    if len(targets_1) == self.batch_size:
                        inputs = np.asarray(inputs)
                        targets_1 = np.asarray(targets_1)
                        targets_2 = np.asarray(targets_2)
                        #print 'target12 ',targets_1,targets_2
                        #targets = np.asarray(targets)
                        # this will not work for boxes
                        #targets = to_categorical(targets)
                        #print targets
                        #print targets[:][0],targets[:][1]
                        #targets_1 = to_categorical(targets[:][0],2)
                        #targets_2 = to_categorical(targets[:][1],101)
                        targets_1 = to_categorical(targets_1,2)
                        targets_2 = to_categorical(targets_2,8)
                        if mode == 'train' or mode == 'val':
                            inputs = self.preprocess_images(inputs)
                        image_data = {'input_1':inputs}
                        targets = {'gender_prediction':targets_1,'age_prediction':targets_2}
                        yield [image_data,targets]

                            #yield self._wrap_in_dictionary(inputs, targets_1,targets_2)
                        #if mode == 'demo':
                            #yield self._wrap_in_dictionary(inputs, targets_1,targets_2)
                        inputs = []
                        targets_1 = []
                        targets_2 =[]
                        targets = []
    def _wrap_in_dictionary(self, image_array, targets):
        return [{'input_1':image_array},
                {'gender_prediction':targets_1},
                {'age_prediction':targets_2}]
