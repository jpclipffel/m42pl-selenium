from setuptools import setup


setup(
  name='m42pl-selenium',
  author='@jpclipffel',
  url='https://github.com/jpclipffel/m42pl-selenium',
  version='1.0.0',
  packages=['m42pl_selenium',],
  install_requires=[
    'm42pl',
    # ---
    'selenium'
  ]
)
