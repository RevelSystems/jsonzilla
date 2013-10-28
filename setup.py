from distutils.core import setup

setup(
    name='pyzilla-json',
    version='0.0.0.1',
    author='Max Korenkov',
    author_email='mkorenkov@gmail.com',
    url='https://github.com/mkorenkov/pyzilla-json',
    py_modules=['pyzilla', 'protocol'],
    license='Apache License, Version 2.0',
    description='Bugzilla JSON-RPC wrapper',
    long_description=open('README.txt').read(),
)
