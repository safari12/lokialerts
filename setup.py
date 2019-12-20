from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='lokialerts',
    version='0.0.1',
    install_requires=requirements,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'lokialerts = lokialerts.__main__:main'
        ]
    }
)
