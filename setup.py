from setuptools import setup, find_packages


requirements = [
    'setuptools',
    'click',
    'python-rocksdb',
    'pooch'
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'pytest-console-scripts']

setup(
    author="M. Hasan Çelik",
    author_email='muhammedhasancelik@gmail.com',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    description="Fast look up interface allel frequency of variants from gnomad with rocksdb",
    install_requires=requirements,
    license="MIT license",
    entry_points='''
        [console_scripts]
        gnomad_rocksdb_download=gnomad_rocksdb.main:cli_gnomad_rocksdb_download
    ''',
    keywords=['genomics', 'gnomad', 'variant', 'allel frequency'],
    name='gnomad_rocksdb',
    packages=find_packages(include=['gnomad_rocksdb']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/muhammedhasan/gnomad_rocksdb',
    version='0.0.2'
)
