This package is used for multi-task without learning effect.
>reference [Disjoint Multi-task Learning between Heterogeneous Human-centric Tasks](https://arxiv.org/pdf/1802.04962.pdf)

Runing script:
``` bash
python ALTERNATIVE_EP.py --dataset_emotion=expw --dataset_pose=aflw --epoch=64 --model=vggFace  --batch_size=32 --is_augmentation=False --is_dropout=False --is_bn=False --weights_decay=0 --is_freezing=False --no_freezing_epoch=0 --P_loss_weights=1 --E_loss_weights=1 --is_naive=False --is_distilled=True distill_t=1 --is_pesudo=False--is_interpolation=False --interpolation_weights=0 --selection_threshold=0 --is_pesudo_confidence=False --is_pesudo_density=False --density_t=0 --is_pesudo_distribution=False --cluster_k=0 
```



