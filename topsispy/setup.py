from setuptools import setup, find_packages

setup(
    name='topsispy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.24.3'  # Specify the desired version of NumPy
    ],
    author='Manan Mehra',
    author_email='mananmehra330@gmail.com',
    description='A Python package for TOPSIS analysis',
    long_description='A Python package for performing TOPSIS analysis on decision matrices.',
    url='https://github.com/Manan2810/topsispy',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
