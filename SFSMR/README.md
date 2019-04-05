This package is used for multi-task learning with manifold learning method
>reference [Semi-supervised Feature Analysis by Mining Correlations among Multiple Tasks](http://de.arxiv.org/pdf/1411.6232)

model: select four outputs including features and predicted labels, predicted labels for cross-entropy loss while features for regularization( l_{2,1} term, trace norm term), setting the parameter is_manifold as True.

* SFSMR: 
``` bash
python CONFUSION_EP_multitask_manifold.py --dataset_emotion=SFEW --dataset_pose=aflw --epoch=64 --model=vggFace  --batch_size=64 --is_augmentation=False --is_dropout=False --is_bn=False --weights_decay=0 --is_freezing=False --no_freezing_epoch=0 --P_loss_weights=1 --E_loss_weights=1 --is_naive=True --is_distilled=False --is_pesudo=False --is_interpolation=False --interpolation_weights=0 --selection_threshold=0 --is_pesudo_confidence=False --is_pesudo_density=False --is_pesudo_distribution=False --cluster_k=0 --is_lnorm=True --is_trace_norm=True
```





