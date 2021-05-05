from distutils.core import setup
from Cython.Build import cythonize

exts = (cythonize('cyfib.pyx'))
setup(ext_modules=cythonize('cyfib.pyx'))