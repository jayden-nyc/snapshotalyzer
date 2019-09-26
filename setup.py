from setuptools import setup

setup(
    name='Snapshotalyzer',
    version='1.0',
    author='Jack',
    author_email='micecomm@gmail.com',
    description='Snapshotalyzer is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/jayden-nyc/snapshotalyzer',
    install_requires=['click','boto3'],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''')
