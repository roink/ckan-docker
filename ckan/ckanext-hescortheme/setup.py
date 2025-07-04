from setuptools import setup, find_packages

setup(
    name='ckanext-hescortheme',
    version='0.1',
    description='HESCOR THEME',
    author='Philipp Schlueter',
    packages=find_packages(),
    entry_points='''
        [ckan.plugins]
        hescortheme=ckanext.hescortheme.plugin:HescorTheme
    '''
)

