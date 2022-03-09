---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Learning Morphological Feature Perturbation for Semi-Supervised Segmentation'
subtitle: ''
summary: ''
authors:
- Mou-Cheng Xu
- Yu-Kun Zhou
- Chen Jin
- Stefano B Blumberg
- Frederick Wilson
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
date: '2022-02-27'
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
publishDate: '2022-02-27T16:59:59.637688Z'
publication_types:
- '1'
abstract: 'We propose MisMatch, a novel consistency-driven semi-supervised segmentation framework which produces predictions that are invariant to learnt feature perturbations. MisMatch consists of an encoder and a two-head decoders. One decoder learns positive attention to the foreground regions of interest (RoI) on unlabelled images thereby generating
dilated features. The other decoder learns negative attention to the foreground on the same
unlabelled images thereby generating eroded features. We then apply a consistency regularisation on the paired predictions. MisMatch outperforms state-of-the-art semi-supervised
methods on a CT-based pulmonary vessel segmentation task and a MRI-based brain tumour
segmentation task. In addition, we show that the effectiveness of MisMatch comes from
better model calibration than its supervised learning counterpart.'
publication: 'Medical Imaging with Deep Learning (MIDL)'
url_pdf: https://openreview.net/forum?id=OL6tAasXCmi
url_code: https://github.com/moucheng2017/Morphological_Feature_Perturbation_SSL
---
