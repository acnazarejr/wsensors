"""Setup script."""

from setuptools import setup, find_packages

VERSION = '0.1.0'
AUTHOR = 'Antonio C. Nazare Jr.'
EMAIL = 'antonio.nazare@dcc.ufmg.br'
REQUIREMENTS = [line for line in open('requirements.txt').read().split('\n') if line != '']

setup(
    name='wsensors',
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    url='https://github.com/acnazarejr/wsensors',
    download_url='https://github.com/acnazarejr/wsensors',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries'
    ],
    description='The WSensors package is a Pythonic module for wearable sensors processing.',
    long_description=open('readme.md').read(),
    keywords='wsensors sensors wearable recognition',
    packages=find_packages(),
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=REQUIREMENTS,
    extras_require={
        'tf': ['tensorflow==1.4.0'],
        'tf-gpu': ['tensorflow-gpu==1.4.0']
    },
    entry_points={
        'console_scripts': [
            'sensorid=wsensors.sensorsid.cli:main'
        ]
    }
)
