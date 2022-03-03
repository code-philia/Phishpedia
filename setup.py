from setuptools import setup, find_packages
from functools import reduce

long_description = """Phishpedia"""
version="0.0.0"

setup(name='phishpedia',
      version="0.0.0",
      description='Phishpedia',
      author='Ruofan Liu',
      author_email='liu.ruofan16@u.nus.edu',
      url='https://github.com/lindsey98/Phishpedia',
      license='Apache License 2.0',
      python_requires='==3.7.*',
      install_requires=[
            'torchsummary',
            'scipy',
            'tldextract',
            'opencv-python',
            'selenium',
            'helium',
            'selenium-wire',
            'webdriver-manager',
            'pandas',
            'numpy',
            'tqdm',
            'Pillow',
            'pathlib',
            'fvcore',
            'pycocotools',
            'scikit-learn',
      ],
      packages=[pkg for pkg in find_packages() if pkg.startswith('phishpedia')],
)