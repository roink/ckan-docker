# -*- coding: utf-8 -*-
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class CustomFacetsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController, inherit=True)

    def dataset_facets(self, facets_dict, package_type):
        # keep existing facets, then add ours
        facets_dict.clear()
        facets_dict['subject']              = toolkit._('Data Pillar')
        facets_dict['language']             = toolkit._('Language') 
        facets_dict['keywords']             = toolkit._('Keywords')
        facets_dict['rights']             = toolkit._('License')
        facets_dict['format']             = toolkit._('File Type')
        facets_dict['geologicalTimeframe'] = toolkit._('Geological Timeframe')
        return facets_dict

    def before_index(self, data_dict):
        values = []
        for entry in data_dict.get('geologicalTimeframes', []):
            if isinstance(entry, dict):
                tf = entry.get('geologicalTimeframe')
                if tf:
                    values.append(tf)
        if values:
            data_dict['geologicalTimeframe'] = values
        return data_dict
