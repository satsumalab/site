---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Bayesian Pseudo Labels: Expectation Maximization for Robust and Efficient Semi Supervised Segmentation"
subtitle: ''
summary: ""

authors:
- Mou Cheng Xu
- Yu Kun Zhou
- Chen Jin
- Marius de Groot
- Daniel C Alexander
- Neil P Oxtoby
- Yipeng Hu
- Joseph Jacob

tags:
- deep learning
- semi supervised
- segmentation
- pseudo labels
- bayesian deep learning
- open access

categories: []
date: '2022-09-27'
lastmod: 2022-10-08T14:43:00Z
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
publishDate: '2022-09-27T21:30:42.00Z'
publication_types:
- '1'
abstract: 'This paper concerns pseudo labelling in segmentation. Our contribution is fourfold. Firstly, we present a new formulation of pseudo-labelling as an Expectation-Maximization (EM) algorithm for clear statistical interpretation. Secondly, we propose a semi-supervised medical image segmentation method purely based on the original pseudo labelling, namely SegPL. We demonstrate SegPL is a competitive approach against state-of-the-art consistency regularisation based methods on semi-supervised segmentation on a 2D multi-class MRI brain tumour segmentation task and a 3D binary CT lung vessel segmentation task. The simplicity of SegPL allows less computational cost comparing to prior methods. Thirdly, we demonstrate that the effectiveness of SegPL may originate from its robustness against out-of-distribution noises and adversarial attacks. Lastly, under the EM framework, we introduce a probabilistic generalisation of SegPL via variational inference, which learns a dynamic threshold for pseudo labelling during the training. We show that SegPL with variational inference can perform uncertainty estimation on par with the gold-standard method Deep Ensemble.'
publication: '*Medical Image Computing and Computer Assisted Interventions (MICCAI)*'
url_pdf: https://link.springer.com/chapter/10.1007/978-3-031-16443-9_56
url_code: https://github.com/moucheng2017/EMSSL
doi: https://doi.org/10.1007/978-3-031-16443-9_56

---
