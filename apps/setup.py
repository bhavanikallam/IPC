from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'TCPIPCSocketServer'
LONG_DESCRIPTION = 'IPC server'

# Setting up
setup(
    name="IPCApp",
    version=VERSION,
    author_email="developer@aline-consulting.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'pendulum', 'scipy']
)
