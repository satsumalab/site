---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Learning to Pay Attention to Mistakes'
subtitle: ''
summary: ''
authors:
- Mou-Cheng Xu
- Neil P. Oxtoby
- Daniel C. Alexander
- Joseph Jacob
tags:
- deep learning
- soft attention
- computer vision
- segmentation
- open access

categories: []
date: '2022-09-06'
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
publishDate: '2020-09-06T16:59:59.637688Z'
publication_types:
- '1'
abstract: 'In convolutional neural network based medical image segmentation, the periphery of
foreground regions representing malignant tissues may be disproportionately assigned as
belonging to the background class of healthy tissues [18][21][24][12][4]. Misclassification of foreground pixels as the background class can lead to high false negative detection rates. In this paper, we propose a novel attention mechanism to directly address such
high false negative rates, called Paying Attention to Mistakes. Our attention mechanism
steers the models towards false positive identification, which counters the existing bias
towards false negatives. The proposed mechanism has two complementary implementations: (a) “explicit” steering of the model to attend to a larger Effective Receptive Field
on the foreground areas; (b) “implicit” steering towards false positives, by attending to
a smaller Effective Receptive Field on the background areas. We validated our methods
on three tasks: 1) binary dense prediction between vehicles and the background using
CityScapes; 2) Enhanced Tumour Core segmentation with multi-modal MRI scans in
BRATS2018; 3) segmenting stroke lesions using ultrasound images in ISLES2018. We
compared our methods with state-of-the-art attention mechanisms in medical imaging,
including self-attention, spatial-attention and spatial-channel mixed attention. Across all
of the three different tasks, our models consistently outperform the baseline models in
Intersection over Union (IoU) and/or Hausdorff Distance (HD). For instance, in the second task, the “explicit” implementation of our mechanism reduces the HD of the best
baseline by more than 26%, whilst improving the IoU by more than 3%. We believe our
proposed attention mechanism can benefit a wide range of medical and computer vision
tasks, which suffer from over-detection of background.'
publication: '*BritishMachineVisionConference*'
url_pdf: https://www.bmvc2020-conference.com/assets/papers/0335.pdf
url_code: https://github.com/moucheng2017/Pay_Attention_To_Mistakes
---
