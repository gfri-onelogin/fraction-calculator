from setuptools import find_packages, setup

REQUIREMENTS = []

ENTRY_POINTS = {
    'console_scripts': [
        'frac-calc = FractionCalculator.fraction-calculator'
    ]
}

setup(
    name='FractionCalculator',
    version='0.0.1',
    description='A quick and dirty fraction calculator',
    url='https://github.com/gfri-onelogin/fraction-calculator',
    author='Geoff Friesen',
    author_email='gfri@protonmail.com',
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    entry_points=ENTRY_POINTS
)
