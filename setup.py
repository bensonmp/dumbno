from setuptools import setup

setup(name='dumbno',
    version='0.6.1',
    zip_safe=True,
    py_modules = ["dumbno"],
    install_requires=[
        "jsonrpclib==0.1.7",
    ],
    entry_points = {
        'console_scripts': [
            'dumbno = dumbno:main',
        ]
    }
)
