This package is used for single-task learning, mainly include emotion, pose, gender and age recognition.

Model selection:
* pretrained model: --model=vggFace
* light model: --model=mini_xception

Runing script:
* Emotion recognition: 
``` bash
python STL_general_train.py --dataset=SFEW[or expw,ferplus] --model=vggFace --epoch=64 --batch_size=32 --is_augmentation=False --is_dropout=False --is_bn=False --weights_decay=0 --is_freezing=False --no_freezing_epoch=0 --task_type=0
```

* Pose recognition: 
``` bash
python STL_general_train.py --dataset=aflw --model=vggFace --epoch=64 --batch_size=32 --is_augmentation=False --is_dropout=False --is_bn=False --weights_decay=0 --is_freezing=False --no_freezing_epoch=0 --task_type=5
```

* Gender recognition: 
``` bash
python STL_general_train.py --dataset=adience[or imdb] --model=vggFace --epoch=64 --batch_size=32 --is_augmentation=False --is_dropout=False --is_bn=False --weights_decay=0 --is_freezing=False --no_freezing_epoch=0 --task_type=10
```

* Age recognition: 
``` bash
python STL_general_train.py --dataset=adience --model=vggFace --epoch=64 --batch_size=32 --is_augmentation=False --is_dropout=False --is_bn=False --weights_decay=0 --is_freezing=False --no_freezing_epoch=0 --task_type=1
```




