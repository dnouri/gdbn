import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

setup(name='gdbn',
      version='0.1',
      description="Pre-trained deep neural networks",
      long_description=README,
      author='George Dahl',
      license='MIT (see license.txt)',
      url='http://www.cs.toronto.edu/~gdahl/',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['gnumpy'],
      )
