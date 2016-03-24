try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Alex Seiden',
    'url': 'https://github.com/aseiden/template',
    'download_url': 'https://github.com/aseiden/template/archive/master.zip',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'template'
}

setup(**config)