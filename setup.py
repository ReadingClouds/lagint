from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='lagint',
    url='https://github.com/ReadingClouds/lagint',
    author='Peter Clark',
    author_email='p.clark@reading.ac.uk',
    # Needed to actually package something
    packages=['lagint', 
              ],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1.0',
    # The license can be anything you like
    license='MIT',
    description='python code to Lagrange interpolate.',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)