import setuptools

setuptools.setup(
    name='{{ app_name }}',
    use_scm_version={'version_scheme': 'post-release'},
    packages=setuptools.find_packages(),
    install_requires=[
        'coverage',
        'django-dynamic-fixture',
        'django-nose',
        'django-webtest',
        'mkdocs',
        'nose-progressive',
        'WebTest',
    ],
    extras_require={
        'dev': ['ipdb', 'ipython'],
        'postgres': ['psycopg2'],
    },
    setup_requires=['setuptools_scm'],
)
