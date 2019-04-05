There are two kinds of training strategise for multitask including joint training and alternative  training and single-task taining

* confusion_MTL is used for joint training to prepare data generator:
   EAP: emotion,age,pose
   EP: emotion,pose
   EGA: emotion,gender,age
   EA: emotion,age
   manifold: generating manifold regularization consists of $l_{1,2}$ norm, trace nom, nuclear norm and Laplacian norm.

* proposed_MTL is used for alternative training to prepare data generator:
   same as above

* pseudo_density_distribution is used for generating weights of confidence score, local density and data distribution and selection critiria:
   $ density_gmm_distribution: density and gmm calculation
   $ pseudo_label_weights: different selection critiria for pseudo labels including distilled knowledge, confidence score, local density and data distibution.


* STL is used for STL training to prepare data generator

