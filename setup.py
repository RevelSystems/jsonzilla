from distutils.core import setup
import re
from setuptools import find_packages

__version__ = "0.0.0.1"


def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            # TODO support version numbers
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'\s*-f\s+', line):
            pass
        else:
            requirements.append(line)

    return requirements


def parse_dependency_links(file_name):
    dependency_links = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'\s*-[ef]\s+', line):
            dependency_links.append(re.sub(r'\s*-[ef]\s+', '', line))

    return dependency_links


setup(
    name='jsonzilla',
    version=__version__,
    author='Max Korenkov',
    author_email='max@revelsystems.com',
    url='https://github.com/RevelSystems/jsonzilla',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    dependency_links=parse_dependency_links('requirements.txt'),
    license='Apache License, Version 2.0',
    description='Bugzilla JSON-RPC wrapper',
    long_description=open('README.txt').read(),
)
