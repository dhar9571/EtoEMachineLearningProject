from setuptools import find_packages, setup

from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='Dharmendra',
    author_email='dk9571288791@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)