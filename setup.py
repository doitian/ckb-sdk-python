import os
import io
from setuptools import setup, find_packages

HERE = os.path.dirname(os.path.realpath(__file__))

README = os.path.join(HERE, 'README.md')
with io.open(README, encoding='utf-8') as f:
    long_description = f.read()

VERSION = os.path.join(HERE, 'ckb', 'version.py')
with io.open(VERSION, encoding='utf-8') as f:
    package = {}
    exec(f.read(), package)
    version = package['VERSION']

setup(name='ckb',
      version=version,
      description='Nervos CKB SDK',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/doitian/ckb-sdk-python',
      author='ian',
      author_email='ian@nervos.org',
      license='MIT',
      packages=find_packages(),
      install_requires=['jsonrpcclient', 'requests', 'typing-extensions'],
      scripts=[],
      zip_safe=False,
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
      ],
      include_package_data=True,
      )
