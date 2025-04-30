Local shared data
=================

Direct local data access
~~~~~~~~~~~~~~~~~~~~~~~~

Mounted data directories:

.. attention::

  The absolute paths for ``~/shared-craas2-ns9988k**`` are actually ``/mnt/craas2-ns9988k**``. A lot of python packages do not accept symbolic links, so please, use ``/mnt/**``.


- ``~/shared-craas2-ns9988k-cmip6-ns9034k/`` NorESM KeyClim and ForCes data.
- ``~/shared-craas2-ns9988k-dl-ns9560k/CAM6_CESM_PPE`` CAM6 output for Perturbed Parameter Experiment

- ``~/shared-craas2-ns9988k-dl-ns9560k/ESGF/CMIP6`` subset of CMIP6 data from ESGF.

- ``~/shared-craas2-ns9988k-ns9252k/escience2025/data`` contains  shared data requested by individual groups

- ``~/shared-craas1-ns9989k-geo4992/catalogs`` - various intake catalogs for local + pangeo data access.

..  - ``./cmip6.json`` local CMIP6 data corresponding to ``~/shared-craas1-nn9989k-cmip6/``

..  - ``./merged-cmip6.json`` same as above but with pangeo catalog merged

..  - ``./cesm-ppe-pi-mon.json`` cesm ppe pre-industrial monthly variables

..  - ``./cesm-ppe.json`` cesm present day variables.

..  - ``~/shared-craas1-ns9989k-geo4992/data/data_group1/``:

..  - ``./data_group1/deposited2022/modis_cdnc_sampling_gridded/`` MODIS based dataset for cloud droplet number concentration from Gryspeerdt et al. (2022, https://amt.copernicus.org/articles/15/3875/2022/)

.. - ``~/shared-craas1-ns9989k-geo4992/data/data_group3/**``:

..  - ``./NYA_radiation/`` Longwave and shortwave radiation observational data from Ny-Ålesund, 2006-2024.

..  - ``./DMPS_ZEP/`` Aerosol size distribution observational data from Zeppelin Observatory, 2000-2020.

..  - ``./echam_salsa_zep/`` Model output from ECHAM-SALSA with nudged surface meteorology, collocated with Zeppelin observatory from 2011-2020. Aerosol, basic meteorology and radiation parameters.

..  - ``./ec-earth/`` variables from ec-earth project.

.. - ``~/shared-craas1-ns9989k-geo4992/data/data_group4/`` Fire emissions from CAMS and MERRA2 + aerosol data from `<https://doi.org/10.5194/acp-24-2059-2024>`_ and `<https://doi.org/10.17043/zeppelin-ebc-2015-2019-1>`_.

.. - ``~/shared-craas1-ns9989k-geo4992/data/data_group6/`` Hysplit(2018-2019), AMS, CCN and cloud radar derived cloud base Updraft data (warm non-precipitating clouds) from Zeppelin (Ny-Ålesund).
  - ``./CMIP6`` additional variables for historical, abrupt-4xCO2, 1pctCO2, ssp119, ssp585 with IPSL and HadGEM3.

.. - ``~/shared-craas1-ns9989k-geo4992/data/data_group6/``  Hysplit (2018-19), AMS, CCN and updraft data (cloud-radar derived) for Zappelin.


.. - ``~/shared-craas1-ns9989k-geo4992/data/data_group7/``:

..  - ``./3D_CloudFraction330m_200701-201512_night_CFMIP2_sat_3.1.2.nc`` GOCCP Cloud fraction
..  - ``./3D_CloudFraction_Phase330m_200701-201512_night_CFMIP2.5_sat_2.9.nc`` GOCCP Cloud fraction by phase
..  - ``./CERES_EBAF-TOA_Ed4.1_Subset_200701-201512_2.5x2.5.nc`` CERES EBAF
..  - ``./amip`` - selected CMIP6 model output from amip experiment
..  - ``./amip+4k`` - selected CMIP6 model output from amip+4k experiment.