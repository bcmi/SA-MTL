## Multi-task learning with disjoint datasets.
we proposed SA-MTL, which can leverage pseudo labels to augment information and  assign different weights to different pseudo samples. We mainly solve two issues
* pseudo labels are noisy

* dataset distribution difference between disjoint datasets



## Comparison among SA-MTL and three groups of baselines, as well as single-task learning:
* In the first group of baselines, we compare with the basic joint training strategy used in All-in-one network [All-in-one]  and alternating training strategy used in DML-LWF [DML-LWF]  for MTL with disjoint datasets.  Specifically, to compare with All-in-one [package 'All-in-one'], we mix training samples from two datasets to train our model in each epoch. To compare with DML-LWF [package 'DML-LWF'] , we use one dataset to train our network in each epoch and alternate between two datasets, in which soft labels are used to avoid forgetting effect. 

* In the second group, we compare with manifold learning based semi-supervised MTL methods , which utilizes manifold regularization on unlabeled training samples. Specifically, to compare with SFSMR [SFSMR] [package 'SFSMR'] we use $l_{2,1}$-norm and trace norm term to generate manifold regularization for label fitness and manifold smoothness. To compare with SLRM [SLRM] [package 'SLRM'], we combine nuclear norm and Laplacian norm for complexity regularization and smooth regularization. 

* In the third group of baselines, we compare with semi-supervised MTL methods LEL-LTN [LEL-LTN] and DCN-AP [DCN-AP], which use pseudo labels to augment multiple tasks with extra supervision information. 
Specifically, to compare with LEL-LTN [package 'LEL-LTN'], which employs label transfer network to tag samples with pseudo labels, we add a label transfer module to the penultimate layer of our network. To compare with DCN-AP[package 'DCN-AP'], which uses label propagation to fill in missing labels similar to multi-label learning, we leverage Markov Random Field (MRF) to refine the pseudo labels based on our predicted labels. 

* Finally, we also compare with Single-Task Learning (STL) [package 'STL'], which uses one separate network for each task without parameter sharing.


[All-in-one]: https://arxiv.org/pdf/1802.04962.pdf
[DML-LWF]: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8107520&tag=1
[SFSMR]: http://de.arxiv.org/pdf/1411.6232
[SLRM]: https://arxiv.org/pdf/1802.09913.pdf
[LEL-LTN]: https://arxiv.org/pdf/1802.09913.pdf
[DCN-AP]: https://arxiv.org/pdf/1609.06426.pdf





