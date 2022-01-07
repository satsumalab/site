---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Evaluation of automated airway morphological quantification for assessing fibrosing lung disease"
subtitle: ''
summary: "Patients with lung damage by scarring typically have abnormally larger airways. This difference in airway size between patients and healthy individuals can be seen with 3D xrays, known as a CT scan. We present a new software program called AirQuant to measure all airways of a patient's CT scan. We compare measurements between 14 healthy individuals and 14 diseased patients. We found that airway disease was worse in the lower lungs and furthermore their airways were also more twisted. Measurements used by AirQuant, has potential as new markers in imaging to help us understand how bad a patient's disease is."

authors:
- Ashkan Pakzad
- Tony Cheung
- Kin Quan
- Nesrin Mogulkoc
- Coline H. M. Van Moorsel
- Brian J. Bartholmai
- Hendrik W. Van Es
- Alper Ezircan
- Frouke Van Beek
- Marcel Veltkamp
- Ronald Karwoski
- Tobias Peikert
- Ryan D. Clay
- Finbar Foley
- Cassandra Braun
- Recep Savas
- Carole Sudre
- Tom Doel
- Daniel C. Alexander
- Peter Wijeratne
- David Hawkes
- Yipeng Hu
- John R Hurst
- Joseph Jacob

tags:
- image analysis
- segmentation
- deep learning
- lung
- airways
- pulmonary fibrosis
- IPF
- open access
- open source
- papers with code

categories: []
date: '2021-11-19'
lastmod: 2022-01-06T14:43:00Z
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
publishDate: '2021-11-19T21:30:42.00Z'
publication_types:
- '3'
abstract: 'Abnormal airway dilatation, termed traction bronchiectasis, is a typical feature of idiopathic pulmonary fibrosis (IPF). Volumetric computed tomography (CT) imaging captures the loss of normal airway tapering in IPF. We postulated that automated quantification of airway abnormalities could provide estimates of IPF disease extent and severity. We propose AirQuant, an automated computational pipeline that systematically parcellates the airway tree into its lobes and generational branches from a deep learning based airway segmentation, deriving airway structural measures from chest CT. Importantly, AirQuant prevents the occurrence of spurious airway branches by thick wave propagation and removes loops in the airway-tree by graph search, overcoming limitations of existing airway skeletonisation algorithms. Tapering between airway segments (intertapering) and airway tortuosity computed by AirQuant were compared between 14 healthy participants and 14 IPF patients. Airway intertapering was significantly reduced in IPF patients, and airway tortuosity was significantly increased when compared to healthy controls. Differences were most marked in the lower lobes, conforming to the typical distribution of IPF-related damage. AirQuant is an open-source pipeline that avoids limitations of existing airway quantification algorithms and has clinical interpretability. Automated airway measurements may have potential as novel imaging biomarkers of IPF severity and disease extent.'
publication: '*arXiv*'
url_pdf: https://arxiv.org/abs/2111.10443
url_code: 'https://github.com/ashkanpakzad/AirQuant'

---
