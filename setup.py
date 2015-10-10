import codecs

from setuptools import setup

from neis import __version__, __author__, __author_email__

with codecs.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyneis',
    version=__version__,

    description='python http client for Neis service(http://neis.go.kr/)',
    long_description=long_description,

    url='https://github.com/HallaZzang/pyneis',

    author=__author__,
    author_email=__author_email__,

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords=['pyneis', 'neis'],

    packages=['neis'],

    install_requires=['requests', 'BeautifulSoup4']
)