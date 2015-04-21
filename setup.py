import setuptools

from {{ app_name }} import __version__

setuptools.setup(
    name='{{ app_name }}',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'coverage',
        'django-dynamic-fixture',
        'django-nose',
        'django-webtest',
        'mkdocs',
        'nose-progressive',
        'tox',
        'WebTest',
    ],
)
