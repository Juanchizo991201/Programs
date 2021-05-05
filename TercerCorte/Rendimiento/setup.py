from distutils.core import setup
from Cython.Build import cythonize
import numpy

exts = (cythonize('functionE_Cython.pyx'))

setup(ext_modules=exts,
      include_dirs=[numpy.get_include()]
      )