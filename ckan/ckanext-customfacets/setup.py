from setuptools import setup, find_packages

setup(
    name='ckanext-customfacets',
    version='0.1',
    description='Add custom facets for scheming fields',
    author='Philipp Schlueter',
    packages=find_packages(),
    entry_points='''
        [ckan.plugins]
        customfacets=ckanext.customfacets.plugin:CustomFacetsPlugin
    ''',
    install_requires=[
        'ckanext-scheming',  # ?
    ],
)

