from distutils.core import setup, Extension

setup(name='python-ftools',
      version='0.1',
      ext_modules=[
          Extension('ftools', ['ftools.c']),
      ])
