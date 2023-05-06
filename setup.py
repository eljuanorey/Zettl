from setuptools import setup, find_packages

setup(
    name='zettl',
    version='0.7.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'zettl=zettl.cli:cli',
        ],
    },
    install_requires=[
        'click',
        'click_aliases',
    ],
    options={
        'bdist_wheel': {
            'universal': True,
            'dist_dir': 'dist',
        },
        'sdist': {
            'dist_dir': 'dist',
            'install_scripts': 'zettl/bin',
        },
    }
)