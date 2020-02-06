# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:17:00 2017

@author: Yoel Cortes-Pena
"""
from setuptools import setup
#from Cython.Build import cythonize
#import numpy

setup(
    name='biosteam',
    packages=['biosteam'],
    license='MIT',
    version='1.0.8',
    description='The Biorefinery Simulation and Techno-Economic Analysis Modules',
    long_description=open('README.rst').read(),
    #ext_modules=cythonize('biosteam/equilibrium/unifac.pyx'),
    #include_dirs=[numpy.get_include()],
    author='Yoel Cortes-Pena',
    install_requires=['pint==0.9', 'ht==0.1.52', 'fluids==0.1.74', 'numba==0.46.0',
                      'scipy==1.3.1', 'IPython==7.9.0', 'colorpalette>=0.3.0',
                      'array_collections==0.1.9', 'free_properties==0.1.9',
                      'pandas==0.25.2', 'graphviz==0.8.3', 'matplotlib==3.1.1',
				  'lazypkg>=1.4', 'chaospy==3.0.11', 'coolprop==6.3.0',
				  'numpy==1.17.3', 'xlrd==1.2.0', 'openpyxl==3.0.0', 'flexsolve',
                      'llvmlite==0.30.0'],
    python_requires=">=3.6",
    package_data=
        {'biosteam': ['_equilibrium/*', 'inspect/*', 'price/*', '_report/*',
                      'utils/*', 'compounds/*',  'reaction/*',
				  'tests/*',
                      'evaluation/*', 
                      'evaluation/evaluation_tools/*',
                      'thermo/*',
                      'thermo/Critical Properties/*',
                      'thermo/Density/*', 
                      'thermo/Electrolytes/*', 
                      'thermo/Environment/*', 
                      'thermo/Heat Capacity/*', 
                      'thermo/Identifiers/*',
                      'thermo/Law/*', 
                      'thermo/Misc/*', 
                      'thermo/Phase Change/*', 
                      'thermo/Reactions/*', 
                      'thermo/Safety/*', 
                      'thermo/Solubility/*', 
                      'thermo/Interface/*', 
                      'thermo/Triple Properties/*', 
                      'thermo/Thermal Conductivity/*', 
                      'thermo/Vapor Pressure/*', 
                      'thermo/Viscosity/*',
                      'units/*',
                      'units/designtools/*',
                      'units/facilities/*',
                      'units/decorators/*',
                      'my_units_defs.txt', 
                      ]},
    platforms=['Windows', 'Mac', 'Linux'],
    author_email='yoelcortes@gmail.com',
    url='https://github.com/yoelcortes/biosteam',
    download_url='https://github.com/yoelcortes/biosteam.git',
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'License :: OSI Approved :: University of Illinois/NCSA Open Source License',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Chemistry',
                 'Topic :: Scientific/Engineering :: Mathematics'],
    keywords='chemical process simmulation bioprocess engineering mass energy balance material properties phase equilibrium CABBI biorefinery biofuel bioproducts',
)