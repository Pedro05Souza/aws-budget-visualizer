from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'click',
        'boto3'
    ],
    entry_points={
        'console_scripts': [
            'aws- = aws.cli.budget_cli:BudgetManagerCLI.cli',
        ]
    }
)