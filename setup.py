#!/usr/bin/env python

import sys
import platform
import setuptools

python_version = sys.version_info[:2]

if python_version < (3, 10):
    raise Exception(
        'SynthSeg requires Python 3.10 or newer (got {}.{}).\n'
        'For legacy Python 3.8 support use the upstream BBillot/SynthSeg.'.format(*python_version)
    )

with open('requirements_python3.10.txt') as f:
    required_packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# On macOS Apple Silicon add tensorflow-metal for GPU acceleration
extras = {}
if platform.system() == 'Darwin' and platform.machine() == 'arm64':
    extras['metal'] = ['tensorflow-metal>=1.1']

setuptools.setup(
    name='SynthSeg',
    version='2.0.1',
    license='Apache 2.0',
    description='Domain-agnostic segmentation of brain scans',
    author='Benjamin Billot',
    url='https://github.com/D3njo/SynthSeg',
    keywords=['segmentation', 'domain-agnostic', 'brain', 'MRI'],
    packages=setuptools.find_packages(),
    python_requires='>=3.10',
    install_requires=required_packages,
    extras_require=extras,
    include_package_data=True,
)
