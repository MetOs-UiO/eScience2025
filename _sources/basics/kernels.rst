Using different kernels in notebooks
====================================


.. note::
  We are using ``mamba`` here which is a drop in replacement for ``conda`` that is generally faster. All commands that work with ``mamba`` should also work with ``conda``.

We provide different conda environments as kernels for processing jupyternotebooks.
You can see them in the launcher when you create a new notebook or choose one in the drop-dowmn menu in the top right corner.
If you want to check which packages are included in the environment you can find the names of the environments available by doing: ``mamba env list``.
To list packages and their versions within the environment use the following command: ``mamba env export -n environment_name --no-builds``.

Available kernels
-----------------

- **minimal**: bare python3.11 environment
- **base**: contains basic packages (mostly not useful for data processing)
- **pangeo-notebook**: environment, built from `Pangeo nootbook v2024.04.05 <https://github.com/pangeo-data/pangeo-docker-images/tree/2024.04.05/pangeo-notebook>`_ extended with ``rioxarray``, ``pyrcel`` and ``geocat`` packages.
- **ml-notebook**: environment, built from `Pangeo ml-nootbook v2024.04.05 <https://github.com/pangeo-data/pangeo-docker-images/tree/2024.04.05/ml-notebook>`_ with added packages:

  .. code-block::

    'gpflow' 
    'scikit-learn'
    'tf-keras'
    'tensorflow-probability'
    'tensorflow'
    'iris'
    'tqdm'
    'cis'
    'ESEM'
    'pyaro'
    'pyaerocom'

  .. attention::
    
    ``pyaero-notebook`` has been removed and latest ``pyaerocom`` added to the ``ml-notebook``.

..
  .. code-block::
..
    'pycel'
    'ipykernel' 
    'scikit-learn'
    'netcdf4'
    'xarray' 
    'pyngl' 
    'proplot' 
    'cartopy' 
    'rioxarray' 
       
    'pandas' 
    'proplot' 
    'seaborn' 
    'cis'


Using the conda environments outside of the course
--------------------------------------------------

.. note::
  
  Too learn more about what conda does and how to make your data analysis reproduce able, check out the code-refinery lesson on `conda-for-data-scientists <https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/01-getting-started-with-conda/index.html>`_.


You can also pipe it to a file to view later or to create same environment somewhere else: ``mamba env export -n <environment name> > environment.yml``. To leave out the build information use add ``--no-builds``.
To create an environment out of this file: ``mamba -n environment_name -f environment.yml``. 



.. attention:: 
  :class: toggle
  :name: Platform specific environments

  The exported environment may be platform specific, f.e. you will see ``platform: linux-64``.
  Recreating the environment on another platform might not work since some of the packages might not be available for your target platform.
  In that case, it's recommended to use containers to reproduce the environment. However it is possible to export platform independent environments by using the ``--no-builds``. 
  Furthermore, conda-lock can be used to create a lock file that solves the dependencies for different platforms and can then be used to recreate the environment on another platform.  