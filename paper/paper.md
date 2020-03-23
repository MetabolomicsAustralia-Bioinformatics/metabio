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

# Statement of Need

``MASTR-Quant`` provides an open-access, transparent way of calculating calibration curves, which would otherwise be inaccessible due to the need to utilize proprietary vendor software, which are usually only compatible with their respective mass spectrometry instruments as well. The methods used by MASTR-Quant are compatible across all vendors.

# 1. Introduction

A multi-omics experiment (e.g. genomics, transcriptomics, proteomics, metabolomics etc.) can be defined as the integration of data across multiple omics layers (Joyce et al., 2006). This can lead to new insights into mechanisms around the genesis of pathogens as well as the creation of novel therapeutics (Civelek et al., 2014; Hasin et al., 2017). Quantitative omics studies allow for more comprehensive integration than non-quantitative studies i.e. reporting is completed in the same units across all omics, and the integration becomes mathematically more robust. The abundance of an analyte is measured and compared against a commercially available standard to obtain either a relative or absolute quantification value. There are several vendor specific software available which are able to extract peak areas and provide absolute concentration values; including Agilent Technologies MassHunter Quantitative Analysis(TM), Shimadzu’s LabSolutions(TM), ThermoFisher’s Xcalibur(TM), Water’s Empower(TM) amongst others. However, being commercial options, they are not freely available and cannot be used for data collected from instruments other than the vendor-specific instruments. In addition to this, calculations completed through spreadsheets can be time consuming and error-prone (http://blogs.nature.com/naturejobs/2017/02/27/escape-gene-name-mangling-with-escape-excel/). This led us to develop a freely available open-source tool, MASTR-Quant that uses processed data from any instrument to obtain quantification results. This freely available software allows users to import data from any analytical instruments including Gas Chromatography Mass Spectrometry (GC-MS) or Liquid Chromatography Mass Spectrometry (LC-MS).

# 2. Methods and Features

MASTR-Quant allows users to efficiently calculate the concentration values of features in mass spectrometry data through visualizing and defining calibration curves based on adjustable parameters.

Data is input to MASTR-Quant in the form of a .csv file that is populated with peak abundances of analytes, which are represented in columns and samples to which they belong represented in rows. A template file is presented in the website for users to download and populate. Any internal standards that may be used are named with a preceding “IS_” tag. Upon uploading an input file, the list of analytes is displayed in a clickable table and all internal standards are displayed in a secondary table. Upon selecting an analyte, its calibration curve is displayed in the main plot with clickable data points. At this point, selecting an internal standard from the secondary table, normalises the data points to the selected internal standard and the resulting calibration curve is plotted. Users can either assign individual internal standards to different analytes or assign the same internal standard to all analytes using the “assign” and “assign all” buttons. Using these options, users are able to assign multiple internal standards to analytes and hence at the end of the workflow they are able to normalise the data based on multiple internal standards.

Similarly, selecting the Reagent Blank subtraction checkbox subtracts the average of any reagent blanks from the data and displays the resulting calibration curve. Using these options, the user can decide which internal standard to assign to the different analytes as well as whether to subtract reagent blanks. In finalising the calibration curve of analytes, users can select and deselect data points in the calibration curve by clicking on them. The graph also has a draggable zoom feature that allows users to zoom into closely clustered data points, especially at the lower end of the curve. In addition, users can set parameter values that influence the curve such as Type (linear, quadratic), Origin (default, forced) and Weight (1/x,1/x2,1/y,1/y2). Selecting the data points that define the curve and setting these parameters dynamically changes the nature of the curve, the equation of the curve and its R2 value. Users can finalise these settings for each analyte by clicking on the “Confirm Regression” button. The table below the main plot shows the final calculated concentration values after applying any internal standard normalisation, reagent blank subtraction and the parameter values of the curve.

# 3. Results

Using the visualisation options detailed above, once the user assigns internal standards (if any), to analytes and has completed defining each analyte’s calibration curve, they can then export all results to an output file using the “confirm” button. Once confirmed, the user is presented with the option to (a) use internal standard normalisation (Y/N), (b) apply regent blank subtraction (Y/N) and (c) normalise the data based on any external numerical measures, such as weight, size etc. In addition, MASTR-Quant allows the user to apply a dilution factor to the final calculated concentration values. Dilution factors need to be applied to the overall concentration calculation to account for any dilutions that occur during the sample extraction process. Upon submission, the above selections along with the analyte-based parameter values are applied and the concentrations calculated. This is presented in both tabular format as well as a downloadable Excel file. The output Excel file contains one sheet for every step of the analyses (raw values, abundance values after internal standard normalisation, coefficient of variation (CV) after internal standard normalisation, abundance values after reagent blank subtraction, CVs after reagent blank subtraction and the final concentration values). In addition, the final sheet of the Excel file stores all the parameter settings used in defining the calibration curve of each analyte.

# Implementation

MASTR-Quant was implemented using Python. The MASTR-Quant server is a Django application and uses MySQL as the backed database. In addition, eCharts and Bootstrap were used to build the web front end. All source code is freely available from https://github.com/MetabolomicsAustralia-Bioinformatics/metabio. In addition to the code, MASTR-Quant is deployed at http://mastr-quant.bio21.unimelb.edu.au. The live site has sample data set for users to test the functions and features of MASTR-Quant.

# Acknowledgements

The authors are grateful to the Victorian Node of Metabolomics Australia, which is funded through the Bioplatforms Australia Pty. Ltd., a National Collaborative Research Infrastructure Strategy (NCRIS), 5.1 biomolecular platforms and informatics investment and co-investment from the Victorian State government and the University of Melbourne. Conflicts of interest: none declared.

# References
