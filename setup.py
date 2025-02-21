from setuptools import find_packages,setup # type: ignore
from setuptools.command.install import install # type: ignore
hypen_e_dot='-e .'
def get_requirements(file):
    with open(file) as f:

        requirements=f.read().splitlines()
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
name='machine_learning',
version='0.1',
packages=find_packages(),
include_package_data=True,
author='Sandhya',
author_email='sandhya025lko@gmail.com',
description='Machine Learning',
install_requires=get_requirements('requirements.txt'),
)
