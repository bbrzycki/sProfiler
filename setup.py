import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ctimer',
    version='0.0.1',
    author='Bryan Brzycki',
    author_email='bbrzycki@berkeley.edu',
    description='Lightweight profiler with checkpoints',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bbrzycki/ctimer',
    project_urls={
        'Source': 'https://github.com/bbrzycki/ctimer'
    },
    packages=setuptools.find_packages(),
#     include_package_data=True,
    install_requires=[
       'numpy>=1.18.1',
#        'scipy>=1.4.1',
#        'astropy>=4.0',
#        'blimpy>=2.0.0',
#        'matplotlib>=3.1.3',
#        'tqdm>=4.47.0',
#        'sphinx-rtd-theme>=0.4.3'
    ],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
