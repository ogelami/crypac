from setuptools import setup, find_packages
import os, sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if sys.version_info < (3,4):
	sys.exit('Python >= 3.4 is required')

setup(name='crypac',
  version='0.1',
  description='Crypac is a tool for packing and encrypting private cryptocurrency assets like private keys and seeds',
  long_description=read('README.md'),
  url='http://github.com/ogelami/crypac',
  author='ogelami',
  author_email='ogelami@gmail.com',
  scripts=['bin/crypac'],
	install_requires=['base58', 'pycryptodome'],
  license='MIT',
  packages=find_packages(),
  zip_safe=False)
