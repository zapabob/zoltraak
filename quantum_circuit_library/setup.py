# setup.py

from setuptools import setup, find_packages

setup()
name= 'zoltraak/quantum_circuit_library'
version='0.1.0',
description='A library for quantum circuits with 4bit=1qubit'
long_description=open('README.md').read(),
long_description_content_type='text/markdown',
author=''
author_email=''
url='https://github.com/zapabob/quantum_circuit_library',
packages=find_packages(),
install_requires=[
'numpy','Zoltraak','niwatoko','qiskit','matplotlib',]
classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python :: 3'10,
        'Programming Language :: Python :: 3'11,
        'Programming Language :: Python :: 3'12,
    ],