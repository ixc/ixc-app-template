from {{ app_name }} import __version__
import setuptools

setuptools.setup(
    name='{{ app_name }}',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'coverage',
        'django-dynamic-fixture',
        'django-nose',
        'django-webtest',
        'nose-progressive',
        'tox',
        'WebTest',
    ],
)
