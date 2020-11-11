import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Daniel Marcelino",
    author_email="dmarcelino@live.com",
    name='ibge',
    license="MIT",
    description='Collection of APIs for the IBGE Data Services in Brazil',
    version='0.0.5',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/danielmarcelino/jota_eleitoral/',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese (Brazilian)'
    ],
    project_urls={
        'Documentation': 'https://github.com/danielmarcelino/jota_eleitoral/blob/master/README.md'
    }
)