# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requirements():
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''
  Modeling and simulation of proton-exchange membrane fuel cells (PEMFC) may work as a powerful tool in the Research &
  development of renewable energy sources. The Open-Source PEMFC Simulation Tool (OPEM) is a modeling tool for
  evaluating the performance of proton exchange membrane fuel cells. This package is a combination of models
  (static/dynamic) that predict the optimum operating parameters of PEMFC. OPEM contained generic models that
  will accept as input, not only values of the operating variables such as anode and cathode feed gas, pressure
  and compositions, cell temperature and current density, but also cell parameters including the active area and
  membrane thickness. In addition, some of the different models of PEMFC that have been proposed in the OPEM,
  just focus on one particular FC stack, and some others take into account a part or all auxiliaries such as
  reformers. OPEM is a platform for collaborative development of PEMFC models.'''


setup(
    name='gopem',
    packages=['gopem'],
    version='0.1',
    description='Open Source GUI Application for OPEM',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Mohammad Mahdi Rahimi,Sepand Haghighi,Kasra Askari,Sarmin Hamidi',
    author_email='opem@ecsim.ir',
    url='https://github.com/ecsim/opem-gui',
    download_url='https://github.com/ecsim/opem-gui/tarball/v0.1',
    keywords="OPEM PEM FC CELL Fuel-Cell Chemistry GUI PyQt",
    project_urls={
        'Webpage': 'http://opem.ecsim.ir',
        'Say Thanks!': 'https://saythanks.io/to/ecsim',
        'Source': 'https://github.com/ecsim/opem',
    },
    platforms=["any"],
    install_requires=get_requirements(),
    python_requires='>=3.4',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Chemistry',
    ],
    license='MIT',
)
