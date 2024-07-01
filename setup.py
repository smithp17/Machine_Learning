"""
This module sets up the ML_PROJECT package configuration using setuptools.
It includes configuration for package name, version, author, dependencies, and more.
"""

from typing import List
from setuptools import find_packages, setup

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return a list of cleaned requirements.
    Each requirement line will have trailing newlines removed,
    and the line '-e .' will be specifically excluded if present.
    """
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
    except FileNotFoundError:
        return []  # Return an empty list if file is not found

    cleaned_requirements = [
        req.replace("\n", "") for req in requirements if req.strip() != '-e .'
    ]
    return cleaned_requirements

setup(
    name='ML_PROJECT',
    version='0.0.1',
    author='Smit Patne',
    author_email='smithp17999@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A machine learning project setup example.',
    url='https://github.com/smithp17/Machine_Learning',  # Updated example URL
)
