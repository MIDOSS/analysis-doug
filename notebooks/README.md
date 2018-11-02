The Jupyter Notebooks in this directory are made by Doug for
sharing of Python code techniques and notes about model results analysis
code.

The links below are to static renderings of the notebooks via
[nbviewer.jupyter.org](https://nbviewer.jupyter.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ##[MOHID-HDF5-to-xarray.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/midoss/analysis-doug/raw/default/notebooks/MOHID-HDF5-to-xarray.ipynb)  
    
    **Development of HDF5 to `xarray.Dataset` Transformation**  
      
    Goal:  
      
    * Use [PyTables](https://www.pytables.org/index.html)  
    to transform contents of MOHID Lagrangian output file  
    into an [`xarray.Dataset`](http://xarray.pydata.org/en/stable/api.html#dataset) object  
      
    This is the development notebook for the `moad_tools.midoss.hdf5_to_xarray()` function.  

* ##[MOHID-hdf5Files.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/midoss/analysis-doug/raw/default/notebooks/MOHID-hdf5Files.ipynb)  
    
    **Explore MODHID hdf5 Files**  
      
    This notebook is an initial exploration of hdf5 output files produced by MOHID.  
      
    MOHID output file types explored:  
      
    * Lagrangian oil particle tracks  
      
    Python libraries explored:  
      
    * [PyNIO](https://www.pyngl.ucar.edu/Nio.shtml)  
    * [h5netcdf](https://github.com/shoyer/h5netcdf)  
    * [h5py](http://docs.h5py.org/en/stable/index.html)  
    * [PyTables](https://www.pytables.org/index.html)  
      
    Summary:  
      
    * PyNIO fails to open the files  
    * h5netcdf successfully opens the files but can't handle groups that contain variables  
    that don't have associated dimension scales  
    * h5py successfully opens the files and allows access to all of their contents,  
    but the interface is a really low level, nested-dict one  
    * PyTables successfully opens the files and allows access to al of their contents  
    via an object interface.  
    The PyTables tutorial also brought the `h5ls` tool to my attention.  
    * The results are organized as Eulerian snapshots,  
    in general both by 2D and 3D slabs of the hydrodynamics model (NEMO or FVCOM) grid,  
    and by particle.  
      
    Next step:  
      
    * Write code to transform PyTables `tables.File` objects into `xarray.Dataset` objects.  


##License

These notebooks and files are copyright 2018
by the the MIDOSS project contributors,
the University of British Columbia,
and Dalhousie University.

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
