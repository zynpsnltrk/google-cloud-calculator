"""
Google Calculator Setup file
"""
from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='gc-calc',
    version='0.1',
    description="Google Cloud Calculator.",
    long_description=readme,
    keywords='google, cloud, gcloud, resources, price, compute engine',
    url='https://github.com/zynpsnltrk/google-cloud-calculator',
    author='Zeynep Sanliturk',
    author_email='zynpsnltrk@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client>=1.7.4,<2',
        'oauth2client>=4.1.3,<5'
    ],
    scripts=['gc-calc'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Environment :: Console',
    ],
    project_urls={
        "Bug Reports": "https://github.com/zynpsnltrk/google-cloud-calculator/issues",
        "Source": "https://github.com/zynpsnltrk/google-cloud-calculator",
        "Say Thanks!": "https://github.com/zynpsnltrk"
    },
    zip_safe=False
)
