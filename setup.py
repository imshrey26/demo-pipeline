from setuptools import setup, find_packages

"""
This will create a overall census-income package and convert all the folders where __init__.py to packages 
"""

setup(name='census-income',
      version='0.0.1',
      author='shrey',
      author_email='imshrey26@gmail.com',
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )