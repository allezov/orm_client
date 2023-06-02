from distutils.core import setup

REQUIRES = [
    'uuid',
    'structlog',
    'sqlalchemy'
]
setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/allezov/orm_client.git',
    license='Apache-2.0 license',
    author='lezov',
    author_email='-',
    install_requires=REQUIRES,
    description='orm_client'
)
