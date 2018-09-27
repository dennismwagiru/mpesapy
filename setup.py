from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mpesapy',
    version='1.0.1',
    url='https://github.com/dennismwagiru/mpesapy',
    license='MIT',
    author='Dennis Mwagiru',
    author_email='dennismwagiru@gmail.com',
    description='Wrapper for M-pesa daraja api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['mpesapy'],
    zip_safe=False,
    install_requires=[
        'requests',
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
