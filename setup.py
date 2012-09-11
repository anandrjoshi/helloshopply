from distutils.core import setup

setup(
    name='HelloShopply',
    version='0.0.1',
    author='Shopply',
    author_email='contactus@shopply.com',
    packages=['helloshopply.code', 'helloshopply.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/MyFirstPackageCreation1/',
    license='LICENSE.txt',
    description='My First Package Creation',
    long_description=open('README.txt').read(),
    install_requires=[
        "pyes >= 0.19.1",
        "tornado >= 2.4",
    ],
)