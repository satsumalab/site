---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'CenTime: Event-conditional modelling of censoring in survival analysis'
subtitle: ''
summary: ''
authors:
- Ahmed H. Shahin
- An Zhao
- Alexander C. Whitehead
- Daniel C. Alexander
- Joseph Jacob
- David Barber
tags:
- deep learning
- survival analysis
- censoring
categories: []
date: '2023-10-29'
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Distributional survival analysis data generation mechanisms.'
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-10-29:00:00:00Z'
publication_types:
- '2'
abstract: 'Survival analysis is a valuable tool for estimating the time until specific events, such as death or cancer recurrence, based on baseline observations. This is particularly useful in healthcare to prognostically predict clinically important events based on patient data. However, existing approaches often have limitations; some focus only on ranking patients by survivability, neglecting to estimate the actual event time, while others treat the problem as a classification task, ignoring the inherent time-ordered structure of the events. Additionally, the effective utilisation of censored samples data points where the event time is unknown is essential for enhancing the model’s predictive accuracy. In this paper, we introduce CenTime, a novel approach to survival analysis that directly estimates the time to event. Our method features an innovative event-conditional censoring mechanism that performs robustly even when uncensored data is scarce. We demonstrate that our approach forms a consistent estimator for the event model parameters, even in the absence of uncensored data. Furthermore, CenTime is easily integrated with deep learning models with no restrictions on batch size or the number of uncensored samples. We compare our approach to standard survival analysis methods, including the Cox proportional-hazard model and DeepHit. Our results indicate that CenTime offers state-of-the-art performance in predicting time-to-death while maintaining comparable ranking performance. Our implementation is publicly available at https://github.com/ahmedhshahin/CenTime.'
publication: 'Medical Image Analysis'
url_pdf: https://www.sciencedirect.com/science/article/pii/S1361841523002761
url_code: https://github.com/ahmedhshahin/CenTime
---
