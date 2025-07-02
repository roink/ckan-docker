# -*- coding: utf-8 -*-
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class CustomFacetsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IFacets)

    def dataset_facets(self, facets_dict, package_type):
        # keep existing facets, then add ours
        facets_dict.clear()
        facets_dict['subject']              = toolkit._('Data Pillar')
        facets_dict['language']             = toolkit._('Language') 
        facets_dict['keywords']             = toolkit._('Keywords')
        facets_dict['rights']             = toolkit._('License')
        facets_dict['format']             = toolkit._('File Type')
        return facets_dict
