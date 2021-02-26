from setuptools import setup, find_packages

install_requires = [
    'aiohttp == 3.7.4',
    'requests == 2.18.4'
]

tests_require = [
    'pytest',
    'pytest-asyncio',
    'pytest-cov',
    'pytest-mock',
    'pytest-mypy',
    'pytest-pycodestyle',
    'pytest-pylint',
    'responses'
]

extras_require = {
    'test': tests_require
}

setup(
    name='python3-practice',
    version="0.0.1",
    description='python3-practice',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
