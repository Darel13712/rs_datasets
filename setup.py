import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rs_datasets',
    version='0.5.0',
    author='Yan-Martin Tamm',
    author_email='darel142857@gmail.com',
    description='Tool for autodownloading recommendation systems datasets',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Darel13712/rs_datasets',
    packages=setuptools.find_packages(),
    install_requires=[
        'datatable',
        'pandas',
        'gdown',
        'pyarrow',
        'tqdm',
        'xlrd',
        'kaggle',
        'py7zr',
        'openpyxl'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
