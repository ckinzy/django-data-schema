# import multiprocessing to avoid this bug (http://bugs.python.org/issue15881#msg170215)
import multiprocessing
assert multiprocessing
import re
from setuptools import setup, find_packages


def get_version():
    """
    Extracts the version number from the version.py file.
    """
    VERSION_FILE = 'data_schema/version.py'
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', open(VERSION_FILE, 'rt').read(), re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in {0}.'.format(VERSION_FILE))


setup(
    name='django-data-schema',
    version=get_version(),
    description='Schemas over dictionaries and models in Django',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ambitioninc/django-data-schema',
    author='Wes Kendall',
    author_email='opensource@ambition.com',
    keywords='Django Data Schema',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
    ],
    license='MIT',
    install_requires=[
        'Django<4.0',
        'django-manager-utils>=1.4.0',
        'fleming>=0.5.0',
        'python-dateutil>=2.2',
    ],
    tests_require=[
        'Django<4.0',
        'django-dynamic-fixture',
        'psycopg2',
        'django-nose',
        'mock',
    ],
    test_suite='run_tests.run_tests',
    include_package_data=True,
)
