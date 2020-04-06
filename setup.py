import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rs_datasets',
    version='0.1.10',
    author='Yan-Martin Tamm, Boris Shminke, Alexey Vasiliev',
    author_email='YYTamm@sberbank.ru',
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
        'xlrd'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)