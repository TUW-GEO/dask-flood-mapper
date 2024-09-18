## Dask based Flood Mapping

This repository contains notebooks that explains how microwave backscattering can be used to map the extent of a flood. We replicate in this exercise the work of Bauer-Marschallinger et al. (2022) on the TU Wien Bayesian-based flood mapping algorithm. This workflow is entirely based on `Dask` and data access via [STAC](https://stacspec.org/en).

To run the workflow

```
git clone git@git.geo.tuwien.ac.at:mschobbe/dask-flood-mapper.git
cd dask-flood-mapper
pip install .
```