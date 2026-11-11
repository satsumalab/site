---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Imaging-based biological age estimation predicts competing mortality risk in lung cancer screening"
subtitle: ''
summary: "People in lung cancer screening are often at high risk of dying from causes other than lung cancer, which limits how much screening can help them. Using CT scans from over 12,000 participants in the SUMMIT lung cancer screening study, we automatically measured signs of ageing in bone, muscle, blood vessels and body fat, and combined them to estimate each person's biological age. People whose bodies looked older than their actual age were at much higher risk of dying from causes other than lung cancer. Because these scans are already taken for screening, biological age could help tailor screening decisions to each person's overall health."

authors:
- Daryl Cheng
- John McCabe
- Tanya Patrick
- Robert Chapman
- Shanshan Wang
- Tianqi Yang
- Adam Szmul
- Mehran Azimbagirad
- Shahab Aslani
- Monica L. Mullin
- Sindhu Bhaarrati Naidu
- Chuen Ryan Khaw
- Alfred So
- The SUMMIT Consortium
- Neal Navani
- Arjun Nair
- John R. Hurst
- Andre Altmann
- Adam Pennycuick
- Daniel C. Alexander
- Neil P. Oxtoby
- Alexandra L. Young
- Matthew Sperrin
- Sam M. Janes
- Joseph Jacob

tags:
- Biological Age
- Lung Cancer Screening
- Computed Tomography
- Disease Progression Modelling
- Competing Risks
- Mortality
- Deep Learning

categories: []
date: '2026-10-15T00:00:00Z'
lastmod: 2026-10-15T00:00:00Z
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

projects: []
publishDate: '2026-10-15T00:00:00Z'
publication_types:
- '2'
abstract: "Lung cancer screening (LCS) participants have a high competing risk of non-lung cancer related death, which limits screening benefit. We hypothesized that imaging-based biological age can identify individuals at higher risk of non-lung cancer mortality. Low dose computed tomography scans from a large LCS trial were retrospectively analyzed. Bone density loss, muscular fat infiltration, vascular calcification, and visceral fat mass were calculated using segmentations from a nnU-Net based deep learning segmentation model. Each participant's age gap, defined as the difference between their estimated biological age and chronological age, was estimated with disease course mapping using a Bayesian mixed-effects model. Disease course map construction used all available longitudinal scan data, whilst individual biological age prediction used baseline scan data only. The performance of age gap as a parameter in competing risk models for non-lung cancer related death versus lung cancer diagnosis was evaluated, following the TRIPOD+AI reporting guideline. We included 29,745 scans from 12,478 participants in the final analysis. Median follow-up was 5 years, representing 58,284 person-years at risk. Multivariable survival models of competing risks were constructed, including the estimated age gap. The subdistribution hazard ratio (sHR) for each decade of age gap for non-lung cancer related death was higher (sHR = 2.0, 95% CI 1.8–2.3), compared to lung cancer diagnosis (sHR = 1.3, 95% CI 1.2–1.5). Addition of age gap improved model concordance of non-lung cancer death compared to a model with clinical variables alone (pooled C-index = 0.69 vs 0.73, difference +0.04, 95% CI 0.03–0.04, p < 0.001). Biological age estimation using an imaging-based disease progression model improves prediction of non-lung cancer related death in lung cancer screening."
publication: '*Scientific Reports*'
doi: 10.1038/s41598-026-75832-2

---
