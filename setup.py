#!/usr/bin/env python
from setuptools import setup

setup(name='bigO',
      version='0.1.1',
      description='Symbolic representation of big-O notation.',
      author='CJ Carey',
      author_email='perimosocordiae@gmail.com',
      url='http://github.com/perimosocordiae/bigO',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
      ],
      packages=['bigO'],
      install_requires=['sympy >= 0.7.5'],
      test_suite='test'
      )
