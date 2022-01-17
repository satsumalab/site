---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Disentangling Human Error from Ground Truth in Segmentation of Medical Images'
subtitle: ''
summary: ''
authors:
- Le Zhang
- Ryutaro Tanno
- Mou-Cheng Xu
- Jin Chen
- Joseph Jacob
- Olga Cicarrelli 
- Frederik Barkhof
- Daniel C. Alexander
tags:
- deep learning
- noisy label
- computer vision
- segmentation
- open access

categories: []
date: '2022-01-17'
lastmod: 2021-11-17T17:00:14Z
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
publishDate: '2020-12-06T16:59:59.637688Z'
publication_types:
- '1'
abstract: 'Recent years have seen increasing use of supervised learning methods for segmentation tasks. However, the predictive performance of these algorithms depends on the quality of labels. This problem is particularly pertinent in the medical image domain, where both the annotation cost and inter-observer variability are high. In a typical label acquisition process, different human experts provide their estimates of the true'' segmentation labels under the influence of their own biases and competence levels. Treating these noisy labels blindly as the ground truth limits the performance that automatic segmentation algorithms can achieve. In this work, we present a method for jointly learning, from purely noisy observations alone, the reliability of individual annotators and the true segmentation label distributions, using two coupled CNNs. The separation of the two is achieved by encouraging the estimated annotators to be maximally unreliable while achieving high fidelity with the noisy training data. We first define a toy segmentation dataset based on MNIST and study the properties of the proposed algorithm. We then demonstrate the utility of the method on three public medical imaging segmentation datasets with simulated (when necessary) and real diverse annotations: 1) MSLSC (multiple-sclerosis lesions); 2) BraTS (brain tumours); 3) LIDC-IDRI (lung abnormalities). In all cases, our method outperforms competing methods and relevant baselines particularly in cases where the number of annotations is small and the amount of disagreement is large. The experiments also show strong ability to capture the complex spatial characteristics of annotators' mistakes.'
publication: '*AdvancesInNeuralInformationProcessingSystems*'
url_pdf: https://proceedings.neurips.cc/paper/2020/hash/b5d17ed2b502da15aa727af0d51508d6-Abstract.html
doi: 
---
