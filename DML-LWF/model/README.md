Main model: models including light network and popular network
* ligth: mini_xception
* popular: vgg, resnet and senet pretrained on VGGFace

Parameters setting:
* model_name: light[mini_xception] or popular[VGGFace]
* input_type: (64,64,1), (224,224,3)
* task_type:1-12, different tasks

Classes of different tasks:
* emotion_classes
* pose_classes
* age_classes
* gender_classes


Overfitting alleviation methon in network
* is_droput
* is_bn
* weights_decay
