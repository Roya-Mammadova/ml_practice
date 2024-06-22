from setuptools import setup, find_packages
from typing import List

HYPEN_E_Dot = '-e.'


def get_requiremet(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readline()
        requirements = [req.replace("\n", "")for req in requirements]
 
        if HYPEN_E_Dot in requirements:
            requirements.remove(HYPEN_E_Dot)
    return requirements


setup(
    name="src",
    version="0.01",
    author="Roya",
    author_email="mroyava@gmail.com",
    install_requires=get_requiremet("requirements.txt"),
    packages=find_packages()
)
