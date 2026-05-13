---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "A computationally frugal, open-source chest CT foundation model for thoracic disease detection in lung cancer screening programmes"
subtitle: ''
summary: "Lung cancer screening uses low-dose chest scans to find cancer early, but these scans can also reveal other diseases before symptoms appear. Interpreting large numbers of scans is challenging due to the limited number of radiologists worldwide. We introduce TANGERINE, an efficient and easy-to-use, open-source AI model that can analyse three-dimensional chest scans efficiently and accurately. The model learns patterns from thousands of scans and can then be adapted to detect lung diseases using only small amounts of new data. TANGERINE performs as well as, or better than, more complex systems while using less computing power. Its open-source design provides a foundation for future tools that could make advanced scan analysis more accessible, supporting earlier diagnosis and improved lung health worldwide."

authors:
- Niccolò McConnell
- Pardeep Vasudev
- Daisuke Yamada
- Daryl Cheng
- Mehran Azimbagirad
- John McCabe
- Shahab Aslani
- Ahmed H. Shahin
- Yukun Zhou
- The SUMMIT Consortium
- Andre Altmann
- Yipeng Hu
- Paul Taylor
- Sam M. Janes
- Daniel C. Alexander
- Joseph Jacob

tags:
- Lung Cancer Screening
- Foundation Models
- Low-Dose Computed Tomography
- Medical Imaging
- Deep Learning
- Thoracic Disease
- Self-Supervised Learning
- Open Source
- TANGERINE

categories: []
date: '2026-02-04T00:00:00Z'
lastmod: 2026-02-04T00:00:00Z
featured: false
draft: false

image:
  caption: ''
  focal_point: ''
  preview_only: false

projects: []
publishDate: '2026-02-04T00:00:00Z'
publication_types:
- '2'
abstract: "Background: Low-dose computed tomography (LDCT) employed in lung cancer screening (LCS) programmes is increasing in uptake worldwide. LCS programmes herald a generational opportunity to simultaneously detect cancer and non-cancer-related early-stage lung disease, yet these efforts are hampered by a shortage of radiologists to interpret scans at scale. Here, we present TANGERINE, a computationally frugal, open-source vision foundation model for volumetric LDCT analysis. Methods: Designed for broad accessibility and rapid adaptation, TANGERINE can be fine-tuned off the shelf for a wide range of disease-specific tasks with limited computational resources and training data. The model is pretrained using self-supervised learning on more than 98,000 thoracic LDCT scans, including the United Kingdom’s largest LCS initiative to date and 27 public datasets. By extending a masked autoencoder framework to three-dimensional imaging, TANGERINE provides a scalable solution for LDCT analysis, combining architectural simplicity, public availability, and modest computational requirements. Results: TANGERINE demonstrates superior computational and data efficiency in a retrospective multi-dataset analysis: it converges rapidly during fine-tuning, requiring significantly fewer graphics processing unit hours than models trained from scratch, and achieves comparable or superior performance using only a fraction of the fine-tuning data. The model achieves strong performance across 14 disease classification tasks, including lung cancer and multiple respiratory diseases, and generalises robustly across diverse clinical centres. Conclusions: TANGERINE’s accessible, open-source, lightweight design lays the foundation for rapid integration into next-generation medical imaging tools, enabling lung cancer screening programmes to pivot from a singular focus on lung cancer detection toward comprehensive respiratory disease management in high-risk populations."
publication: '*Communications Medicine*'
doi: 10.1038/s43856-025-01328-1
url_pdf: https://www.nature.com/articles/s43856-025-01328-1.pdf
url_code: https://github.com/niccolo246/mae_reconstruction

---

