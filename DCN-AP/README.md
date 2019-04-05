This package is used for multi-task learning with label propogation.
>reference [From Facial Expression Recognition to Interpersonal Relation Prediction](https://arxiv.org/pdf/1609.06426.pdf)

* DCN-AP: 
``` bash
python CONFUSION_EP_multitask.py --dataset_emotion=SFEW --dataset_pose=aflw --epoch=64 --model=vggFace  --batch_size=64 --is_augmentation=False --is_dropout=False --is_bn=False --weights_decay=0 --is_freezing=False --no_freezing_epoch=0 --P_loss_weights=1 --E_loss_weights=1 --is_naive=False --is_distilled=False --is_pesudo=True --is_interpolation=False --interpolation_weights=0 --selection_threshold=0 --is_pesudo_confidence=False --is_pesudo_density=False --is_pesudo_distribution=False --cluster_k=0 --is_MRF=True
```



