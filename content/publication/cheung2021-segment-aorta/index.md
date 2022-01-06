---
title: "A computationally efficient approach to segmentation of the aorta and coronary arteries using deep learning"
authors:
- Tony Cheung
- Robert Bell
- Arjun Nair
- Leon Menezies
- Riyaz Patel
- Simon Wan  
- Kacy Chou
- Jiahang Chen
- Ryo Torii
- Rhodri Davies
- James Moon
- Daniel C. Alexander
- Joseph Jacob
date: "2021-02-18T00:00:00Z"
doi: "10.1101/2021.02.18.21252005"

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: '*medRxiv*'
publication_short: ""

abstract: A fully automatic two-dimensional Unet model is proposed to segment aorta and coronary arteries in computed tomography images. Two models are trained to segment two regions of interest, (1) the aorta and the coronary arteries or (2) the coronary arteries alone. Our method achieves 91.20% and 88.80% dice similarity coefficient accuracy on regions of interest 1 and 2 respectively. Compared with a semi-automatic segmentation method, our model performs better when segmenting the coronary arteries alone. The performance of the proposed method is comparable to existing published two-dimensional or three-dimensional deep learning models. Furthermore, the algorithmic and graphical processing unit memory efficiencies are maintained such that the model can be deployed within hospital computer networks where graphical processing units are typically not available.

# Summary. An optional shortened abstract.
summary:

tags:
- deep learning
- segmentation
- computed tomography
- aorta
- heart
- open access

featured: false

# links:
# - name: ""
#   url: ""
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides:
---
