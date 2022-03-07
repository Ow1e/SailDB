from setuptools import setup

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='saildb',
    version='0.1',    
    description='A high performing JSON alternative for speed.',
    url='https://github.com/Ow1e/SailDB',
    author='Owen Shaule',
    author_email='ow1e3@protonmail.com',
    license='',
    keywords=["python", "database"],
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    packages=['saildb'],
    install_requires=[],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)