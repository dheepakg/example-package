from setuptools import setup, find_packages

setup(
    name='export-sys-dtls',
    version='0.0.1',
    description='Captures system details in a flat file',
    url='https://github.com/dheepakg/example-package',
    author='deegovee',
    author_email='sslvgdek@gmail.com',

    packages=find_packages(exclude=['docs','tests']),
    install_requires=['os','platforms','time','datetime'],
    package_data={
        'sample':['app.py']
    },
    entry_points={
        'console_scripts':['hello=example_package.cli:say_hello',], #.exe file gets created here

    },
    license='MIT', #Just giving a license for time-being,
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        #'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
		
    ]

)