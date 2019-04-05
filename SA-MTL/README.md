This package is used for our proposed method, pseudo labels selection combining confidence score, local density and data distribution.

Runing script:
``` bash
python ALTERNATIVE_EP.py  --dataset_emotion=expw --dataset_pose=aflw --epoch=64 --model=vggFace  --batch_size=32 --is_augmentation=False --is_dropout=False --is_bn=False --weights_decay=0 --is_freezing=False --no_freezing_epoch=0 --P_loss_weights=1 --E_loss_weights=1 --is_naive=False --is_distilled=False distill_t=2 --is_pesudo=True --is_interpolation=False --interpolation_weights=0 --selection_threshold=0.8 --is_pesudo_confidence=True --is_pesudo_density=True --density_t=0.6 --is_pesudo_distribution=True --cluster_k=3 
```

Explanation:
* Dataset setting: --dataset_emotion [Expw, Fer+, Fer2013, SFEW], --dataset_pose [AFLW]
* Model setting: --model [VGGFace, mini_xception]
* Training tricks: --is_augmentation=False --is_dropout=False --is_bn=False --weights_decay=0 --is_freezing=False --no_freezing_epoch=0 [data augmentation, dropout, batchnormalization, weights decay, two-stage training]
* Multi-task hyperparameter: --P_loss_weights=1 --E_loss_weights=1 [weights of different tasks]
* Core methods: 
   $ --is_naive=True: not generate pseudo labels

   $ --is_distilled=True, --distill_t: only leverage distilled knowledge to preserve information, distill_t is the temperature

   $ --is_pesudo=True: generateb pseudo labels to augment infromation

   $ --is_interpolation=True: generate interpolated labels combining distilled knowledge and pseudo labels with selected weights, otherwise adopt hard selection method to select high-confidence pseudo labels to augment information, while distilled knowledge is adopt to preserver information for those low-confidence pseudo labels 

   $ --selection_threshold: select pseudo labels for hard selection method

   $ --is_pesudo_confidence=True: leveage confidence score to generate pseudo labels weights

   $ --is_pesudo_density=True, --density_t=0.6: leverage local density to generate pseudo labels weights

   $ --is_pesudo_distribution=True, --cluster_k=3 : leverage MMD and EMD to generate pseudo labels weights

``` 



