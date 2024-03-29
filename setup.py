from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='superplugger',
    url='https://github.com/psytron/superplugger',
    author='Miggler McMiggles',
    author_email='miggler@miggler.com',
    # Needed to actually package something
    packages=['superplugger'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.3',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)