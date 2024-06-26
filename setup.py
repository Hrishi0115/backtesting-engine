from setuptools import setup, find_packages

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Filter out comments and empty lines
        requirements = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
        return requirements

setup(
    name='backtesting_engine',
    version='0.1',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            # if you have any scripts to run
        ],
    },
)
