---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Deep Learning Based Long Term Mortality Prediction in the National Lung Screening Trial"
subtitle: ''
summary: ""

authors:
- Yaozhi Lu
- Shahab Aslani
- Mark Emberton
- Daniel C. Alexander
- Joseph Jacob

tags:
- computed tomography
- computer vision
- deep learning
- lung
- lung screening trial
- mortality
- saliency map

categories: []
date: '2022-01-13'
lastmod: 2022-01-13T00:00:00Z
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
publishDate: '2022-01-13T00:00:00Z'
publication_types:
- '3'
abstract: 'In this study, the long-term mortality in the National Lung Screening Trial (NLST) was investigated using a deep learning-based method. Binary classification of the non-lung-cancer mortality (i.e. cardiovascular and respiratory mortality) was performed using neural network models centered around a 3D-ResNet. The models were trained on a participant age, gender, and smoking history matched cohort. Utilising both the 3D CT scan and clinical information, the models can achieve an AUC of 0.73 which outperforms humans at cardiovascular mortality prediction. By interpreting the trained models with 3D saliency maps, we examined the features on the CT scans that correspond to the mortality signal. The saliency maps can potentially assist the clinicians’ and radiologists’ to identify regions of concern on the image that may indicate the need to adopt preventative healthcare management strategies to prolong the patients’ life expectancy.'
publication: '*medRxiv*'
url_pdf: https://www.medrxiv.org/content/10.1101/2022.01.12.22269152v1
#url_code: 'https://github.com/

---
