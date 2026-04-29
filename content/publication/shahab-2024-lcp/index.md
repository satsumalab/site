---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Exploring Fairness and Performance Drivers Across State-of-the-Art Pulmonary Nodule Detection Algorithms"
subtitle: ''
summary: ""

authors:
- John McCabe
- et al.
- Joseph Jacob
- Carole H. Sudre

tags:
- Computer-aided diagnosis
- Computed tomography
- Lung cancer
- Lung Cancer Screening
- Deep learning

categories: []
date: '2025-12-21'
lastmod: 2025-12-21
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
# Associate this post with one or more of your projects.
# Simply enter your project's folder or file name without extension.
# E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
# Otherwise, set `projects = []`.
projects: []
publishDate: '2025-12-21'
publication_types:
- '2'
abstract: 'Lung cancer is the leading cause of cancer-related deaths in the UK. Its high mortality rate is primarily due to its asymptomatic nature in the early stages, leading to late-stage diagnoses. However, effective early detection methods, such as Low-Dose Computed Tomography (LDCT), and treatments for early-stage disease make lung cancer an ideal candidate for screening. The UK Government aims to implement a national lung cancer screening programme targeting high-risk populations by 2029. This will significantly increase the workload on an already stretched radiology workforce, driving the adoption of computer-aided detection (CADe) systems to support radiologists. The datasets used to train these algorithms are typically drawn from previous lung cancer screening trials and studies (National Lung Screening Trial Research Team (2011); de Koning (2020)), which often lack balanced representation of protected groups, such as sex and ethnicity. This project examines whether training nodule detection algorithms on low-dose computed tomography (LDCT) scans from a London-based lung screening study, where these groups are typically under-represented, affects algorithm performance for under-represented categories. Our results indicate that overall performance remains equitable across all categories, even when trained on unbalanced datasets. The discriminative performance of deep learning-based pulmonary nodule detection algorithms is primarily driven by the composition of the dataset, specifically, the relative proportion of nodule types and sizes, rather than by protected attributes such as sex or ethnic group. The features learned from the nodules themselves drive detection outcomes, meaning that in populations where the prevalent nodule characteristics closely match the training data, performance is likely to be strong. While this study found no demographic disparities for nodule detection, there is no guarantee that this will be true across all populations, particularly those in populations where cancer risk predominates within different nodule distributions. This study provides an early assessment of performance variations of deep learning models across under-represented groups within a standard lung cancer screening dataset. While previous research has focused on improving how well nodule detection algorithms identify pulmonary nodules, this study uniquely focuses on demographic performance disparities and the impact of training data composition and algorithm design on model generalisability. The findings highlight critical considerations for the deployment of CADe systems in lung cancer screening, ensuring equitable performance across diverse patient populations.'
publication: '*MELBA Journal-Special issue on FAIMI*'
doi: 10.59275/j.melba.2025-6838

---
