from setuptools import find_packages, setup
from typing import List
from pathlib import Path

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Get the list of requirements from the specified file.

    :param file_path: Path to the requirements file.
    :return: List of requirements.
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='Customer Churn Prediction',
    version='0.0.1',
    author='Vinay',
    author_email='vinayc.gorantla@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(Path('requirements.txt'))
)
