from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'gokart',
]

setup(
    name={{cookiecutter.package_name}},
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description={{cookiecutter.package_description}},
    long_description=long_description,
    long_description_content_type="text/markdown",
    author={{cookiecutter.author}},
    license={{cookiecutter.license}},
    packages=find_packages(),
    install_requires=install_requires,
    test_suite='test')
