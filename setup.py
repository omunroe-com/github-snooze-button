from setuptools import setup

versionfile = 'snooze/version.py'
with open(versionfile, 'rb') as f:
    exec(compile(f.read(), versionfile, 'exec'))

setup(
    name='github-snooze-button',
    version=__version__,
    url='https://github.com/tdsmith/github-snooze-button',
    license='MIT',
    author='Tim D. Smith',
    author_email='poet@tim-smith.us',
    description='Snooze button for Github issues',
    packages=['snooze'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
    install_requires=['PyGithub', 'boto'],
)