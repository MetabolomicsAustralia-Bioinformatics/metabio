# MASTR-Quant

## Overview

Targeted analysis in mass spectrometry uses a calibration curve to compute the concentration of a substance, by comparison to a set of samples of known concentration. This is canonically done by fitting a straight line of best fit, in a linear regression, to samples with known concentrations and abundance values. New samples with known abundance values but unknown concentrations can then be computed via simple linear interpolation using this fitted linear model.

MASTR-Quant is an open-source web application that allows users to calculate the concentration values of features in mass spectrometry data through visualizing and defining calibration curves based on a range of adjustable parameters. MASTR-Quant presents the user with options including and excluding data points to define linear or quadratic calibration ranges. The tool also includes options to assign individual internal standards to specific analytes by applying weighting factors, background subtraction and dilution ratios, normalization of the data based on internal standards and other external measurements, and the option for assessing the quality of data through the calculation of coefficient of variation values of each sample group. The final output is downloadable as an Excel file with multiple sheets containing detailed results of the individual steps involved in the calculation process.

## Statement of Need

MASTR-Quant provides an open-access, transparent way of calculating calibration curves, which would otherwise be inaccessible due to the need to utilize proprietary vendor software, which are usually only compatible with their respective mass spectrometry instruments as well. The methods used by MASTR-Quant are compatible across all vendors.

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
