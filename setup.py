from setuptools import setup, find_packages

setup(
    name='dataPreprocessor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk',
    ],
    description='A recoded data preprocessing library for handling various data cleaning and transformation tasks. The library includes classes for text cleaning, missing value imputation, one-hot encoding and more.',
    author='fatmanur caliskan, cihan yilmaz',
    author_email='fatmanur.caliskan@stu.fsm.edu.tr, cihan.yilmaz@stu.fsm.edu.tr',
    url='.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
