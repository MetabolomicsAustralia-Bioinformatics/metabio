---
title: 'MASTR-Quant: An Open-Source Web-based Software Tool for the Quantitive Analysis of Mass Spectrometry-based Data'
tags:
  - Python
  - Django
  - Metabolomics
  - Mass spectrometry
authors:
  - name: Ruobing Leng
    affiliation: 1
  - name: Komal Kanojia
    affiliation: 2
  - name: Konstantinos Kouremenos
    affiliation: "2, 3"
  - name: Thusitha Rupasinghe
    affiliation: 2
  - name: Ute Roessner
    affiliation: 2
  - name: Malcolm McConville
    affiliation: 2
  - name: Richard O. Sinnott
    affiliation: 1
  - name: Saravanan Dayalan
    affiliation: "2, 4"
  - name: Vinod K. Narayana
    affiliation: 2
affiliations:
 - name: School of Computing and Information Systems, The University of Melbourne, Victoria, Australia
   index: 1
 - name: Metabolomics Australia, Bio21 Institute of Molecular Science and Biotechnology, The University of Melbourne, Parkville, Victoria, Australia
   index: 2
 - name: Trajan Scientific and Medical, Ringwood, Victoria, Australia
   index: 3
 - name: CSL Ltd, Parkville, Victoria 3010, Australia
   index: 4
date: 31 Dec 2019
bibliography: paper.bib
---

# Summary

Targeted analysis in mass spectrometry uses a calibration curve to derive the concentration of a substance, by comparison to a set of samples of known concentration. This is canonically done by a form of linear regression.

``MASTR-Quant`` is an open-source, web application that allows users to calculate the concentration values of features in mass spectrometry data through visualizing and defining calibration curves based on a range of adjustable parameters. ``MASTR-Quant`` presents the user with options including and excluding data points to define linear or quadratic calibration ranges. The tool also includes options to assign individual internal standards to specific analytes by applying weighting factors, background subtraction and dilution ratios, normalization of the data based on internal standards and other external measurements, and the option for assessing the quality of data through the calculation of coefficient of variation values of each sample group. The final output is downloadable as an Excel file with multiple sheets containing detailed results of the individual steps involved in the calculation process.

# Acknowledgements

The authors are grateful to the Victorian Node of Metabolomics Australia, which is funded through the Bioplatforms Australia Pty. Ltd., a National Collaborative Research Infrastructure Strategy (NCRIS), 5.1 biomolecular platforms and informatics investment and co-investment from the Victorian State government and the University of Melbourne. Conflicts of interest: none declared. 

# References
