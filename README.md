<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>

# Bootstrapping tools

[![codecov](https://codecov.io/gh/IslasGECI/bootstrapping_tools/graph/badge.svg?token=RY807ST1T1)](https://codecov.io/gh/IslasGECI/bootstrapping_tools)
![example branch parameter](https://github.com/IslasGECI/bootstrapping_tools/actions/workflows/develop.yml/badge.svg)
![licencia](https://img.shields.io/github/license/IslasGECI/bootstrapping_tools)
![languages](https://img.shields.io/github/languages/top/IslasGECI/bootstrapping_tools)
![commits](https://img.shields.io/github/commit-activity/y/IslasGECI/bootstrapping_tools)
![PyPI - Version](https://img.shields.io/pypi/v/bootstrapping_tools)


Python package for bootstrap resampling by blocks on ecological time series data.

Estimates population growth rates (λ) by fitting a power law model (`N(t) = N₀ · λᵗ`) to seasonal count data and computing confidence intervals via block resampling. Designed for wildlife monitoring datasets (e.g., seabird burrow counts on Mexican Pacific islands).

## Key features

- **Block resampling** — preserves temporal autocorrelation in time series.
- **Power law fitting** — estimates growth rate λ from seasonal population counts.
- **Confidence intervals** — bootstrap-derived intervals with p-value computation.
- **LaTeX output** — formatted interval strings for inclusion in publications.
- **Abstract base class** — extensible `AbstractSeriesBootstrapper` for custom parametrizers.

## Installation

```bash
pip install bootstrapping_tools
```
