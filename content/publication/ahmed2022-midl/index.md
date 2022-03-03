---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Survival Analysis for Idiopathic Pulmonary Fibrosis using CT Images and Incomplete Clinical Data'
subtitle: ''
summary: ''
authors:
- Ahmed H. Shahin
- Joseph Jacob
- Daniel C. Alexander
- David Barber
tags:
- deep learning
- survival analysis
- IPF
- interstitial lung diseases
- neural networks

categories: []
date: '2022-02-28'
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
publishDate: '2022-02-28T16:59:59.637688Z'
publication_types:
- '1'
abstract: 'Idiopathic Pulmonary Fibrosis (IPF) is an inexorably progressive fibrotic lung disease with a variable and unpredictable rate of progression. CT scans of the lungs inform clinical assessment of IPF patients and contain pertinent information related to disease progression. In this work, we propose a multi-modal method that uses neural networks and memory banks to predict the survival of IPF patients using clinical and imaging data. The majority of clinical IPF patient records have missing data (e.g. missing lung function tests). To this end, we propose a probabilistic model that captures the dependencies between the observed clinical variables and imputes missing ones. This principled approach to missing data imputation can be naturally combined with a deep survival analysis model. We show that the proposed framework yields significantly better survival analysis results than baselines in terms of concordance index and integrated Brier score. Our work also provides insights into novel image-based biomarkers that are linked to mortality.'
# publication: '*AdvancesInNeuralInformationProcessingSystems*'
url_pdf: https://openreview.net/forum?id=YWDmiiJ4hYP
url_code: https://github.com/ahmedhshahin/IPFSurv
---
