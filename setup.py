import os.path

from setuptools import setup, find_packages

version = ''

root_dir = os.path.abspath(os.path.dirname(__file__))

readme_file = os.path.join(root_dir, 'README.md')
with open(readme_file, encoding='utf-8') as f:
    long_description = f.read()

version_module = os.path.join(root_dir, 'src', 'pyplane', 'version.py')
with open(version_module, encoding='utf-8') as f:
    exec(f.read())

setup(
    name='pyplane',
    version=version,
    description='An unofficial Python Plane.so API Driver',
    long_description=long_description,
    url='https://github.com/nyorf/pyplane',
    author='Dmitry Dolgov',
    author_email='me@nyorf.com',
    license='MPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Topic :: Internet',
        'Topic :: Utilities'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires=">=3.9",
    install_requires=[
        'wheel==0.45.0',
        'anyio==4.6.2.post1',
        'certifi==2024.8.30',
        'exceptiongroup==1.2.2',
        'h11==0.14.0',
        'httpcore==1.0.6',
        'httpx==0.27.2',
        'idna==3.10',
        'sniffio==1.3.1',
        'tenacity==9.0.0',
        'typing_extensions==4.12.2'
    ],
)
