from setuptools import setup

setup(
    name='mpesapy',
    version='1',
    packages=['mpesapy'],
    url='https://github.com/dennismwagiru/mpesapy',
    license='MIT',
    author='Joel',
    author_email='dennismwagiru@gmail.com',
    description='Wrapper for M-pesa daraja api',
    install_requires=[
          'requests',
      ],
      zip_safe=False
)
