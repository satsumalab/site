---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'MisMatch: Calibrated Segmentation via Consistency on Differential Morphological Feature Perturbations with Limited Labels'
subtitle: ''
summary: ''
authors:
- Mou-Cheng Xu
- Yu-Kun Zhou
- Chen Jin
- Marius de Groot
- Daniel C. Alexander
- Neil P. Oxtoby*
- Joseph Jacob*
tags:
- deep learning
- semi supervised
- segmentation
- learning augmentation
- open access

categories: []
date: '2023-05-10'
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-05-10T16:59:59.637688Z'
publication_types:
- '1'
abstract: 'Semi-supervised learning (SSL) is a promising machine learning paradigm to address the ubiquitous issue of label scarcity in medical imaging. The state-of-the-art SSL methods in image classification utilise consistency regularisation to learn unlabelled predictions which are invariant to input level perturbations. However, image level perturbations violate the cluster assumption in the setting of segmentation. 
Moreover, existing image level perturbations are hand-crafted which could be sub-optimal. 
In this paper, we propose MisMatch, a semi-supervised segmentation framework based on the consistency between paired predictions which are derived from two differently learnt morphological feature perturbations. 
MisMatch consists of an encoder and two decoders. 
One decoder learns positive attention for foreground on unlabelled data thereby generating dilated features of foreground. 
The other decoder learns negative attention for foreground on the same unlabelled data thereby generating eroded features of foreground. 
We normalise the paired predictions of the decoders, along the batch dimension. 
A consistency regularisation is then applied between the normalised paired predictions of the decoders. 
We evaluate MisMatch on four different tasks. 
Firstly, we develop a 2D U-net based MisMatch framework and perform extensive cross-validation on a CT-based pulmonary vessel segmentation task and show that MisMatch statistically outperforms state-of-the-art semi-supervised methods. 
Secondly, we show that 2D MisMatch outperforms state-of-the-art methods on an MRI-based brain tumour segmentation task. 
We then further confirm that 3D V-net based MisMatch outperforms its 3D counterpart based on consistency regularisation with input level perturbations, on two different tasks including, left atrium segmentation from 3D CT images and whole brain tumour segmentation from 3D MRI images. 
Lastly, we find that the performance improvement of MisMatch over the baseline might originate from its better calibration. 
This also implies that our proposed AI system makes safer decisions than the previous methods.'
publication: 'IEEE Transactions on Medical Imaging (TMI)'
url_pdf: https://ieeexplore.ieee.org/document/10121397
url_code: https://github.com/moucheng2017/Morphological_Feature_Perturbation_SSL
---
