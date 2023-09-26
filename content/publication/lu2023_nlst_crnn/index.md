---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "A hybrid CNN-RNN approach for survival analysis in a Lung Cancer Screening study"
subtitle: ''
summary: ""

authors:
- Yaozhi Lu
- Shahab Aslani
- An Zhao
- Ahmed Shahin
- David Barber
- Mark Emberton
- Daniel C. Alexander
- Joseph Jacob

tags:
- computed tomography
- computer vision
- cox regression
- deep learning
- longitudinal data
- lung
- lung screening trial
- saliency map

categories: []
date: '2023-08-03'
lastmod: 2023-09-26T00:00:00Z
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
publishDate: '2023-08-03T00:00:00Z'
publication_types:
- '2'
abstract: 'In this study, we present a hybrid CNN-RNN approach to investigate long-term survival of subjects in a lung cancer screening study. Subjects who died of cardiovascular and respiratory causes were identified whereby the CNN model was used to capture imaging features in the CT scans and the RNN model was used to investigate time series and thus global information. To account for heterogeneity in patients' follow-up times, two different variants of LSTM models were evaluated, each incorporating different strategies to address irregularities in follow-up time. The models were trained on subjects who underwent cardiovascular and respiratory deaths and a control cohort matched to participant age, gender, and smoking history. The combined model can achieve an AUC of 0.76 which outperforms humans at cardiovascular mortality prediction. The corresponding F1 and Matthews Correlation Coefficient are 0.63 and 0.42 respectively. The generalisability of the model is further validated on an ‘external’ cohort. The same models were applied to survival analysis with the Cox Proportional Hazard model. It was demonstrated that incorporating the follow-up history can lead to improvement in survival prediction. The Cox neural network can achieve an IPCW C-index of 0.75 on the internal dataset and 0.69 on an external dataset. Delineating subjects at increased risk of cardiorespiratory mortality can alert clinicians to request further more detailed functional or imaging studies to improve the assessment of cardiorespiratory disease burden. Such strategies may uncover unsuspected and under-recognised pathologies thereby potentially reducing patient morbidity.'
publication: 'Heliyon'
url_pdf: https://doi.org/10.1016/j.heliyon.2023.e18695
url_code: https://github.com/aeroelasticitylu/LRsurvival_CRNN 

---
