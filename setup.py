from setuptools import setup, find_packages # type: ignore

setup(
    name='Fast_Friendly_Python',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    description='Una biblioteca para facilitar la escritura de código más legible y de alto nivel.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pipQuasar//FFpython',
    author='Tobias Ezequiel Pereyra',
    author_email='mftoba963@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)