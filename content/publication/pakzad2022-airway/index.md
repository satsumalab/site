---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Airway measurement by refinement of synthetic images improves mortality prediction in idiopathic pulmonary fibrosis"
subtitle: ''
summary: ""

authors:
- Ashkan Pakzad
- Mou Cheng Xu
- Tony Cheung
- Marie Vermant
- Tinne Goos
- Laurens J De Sadeleer
- Stijn E Verleden
- Wim A Wuyts
- John R Hurst
- Joseph Jacob

tags:
- image analysis
- deep learning
- synthetic data
- model evaluation
- lung
- airways
- bronchiectasis
- IPF

categories: []
date: '2022-10-08'
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
publishDate: '2022-10-08T21:30:42.00Z'
publication_types:
- '1'
abstract: 'Several chronic lung diseases, like idiopathic pulmonary fibrosis (IPF) are characterised by abnormal dilatation of the airways. Quantification of airway features on computed tomography (CT) can help characterise disease severity and progression. Physics based airway measurement algorithms that have been developed have met with limited success, in part due to the sheer diversity of airway morphology seen in clinical practice. Supervised learning methods are not feasible due to the high cost of obtaining precise airway annotations. We propose synthesising airways by style transfer using perceptual losses to train our model: Airway Transfer Network (ATN). We compare our ATN model with a state-of-the-art GAN-based network (simGAN) using a) qualitative assessment; b) assessment of the ability of ATN and simGAN based CT airway metrics to predict mortality in a population of 113 patients with IPF. ATN was shown to be quicker and easier to train than simGAN. ATN-based airway measurements showed consistently stronger associations with mortality than simGAN-derived airway metrics on IPF CTs. Airway synthesis by a transformation network that refines synthetic data using perceptual losses is a realistic alternative to GAN-based methods for clinical CT analyses of idiopathic pulmonary fibrosis. Our source code can be found at https://github.com/ashkanpakzad/ATN that is compatible with the existing open-source airway analysis framework, AirQuant.'
publication: '*MICCAI Workshop on Deep Generative Models*'
doi: 10.1007/978-3-031-18576-2_11
url_pdf: https://arxiv.org/abs/2208.14141
url_code: 'https://github.com/ashkanpakzad/ATN'

---
