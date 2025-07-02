# -*- coding: utf-8 -*-
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class CustomFacetsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IFacets)

    def dataset_facets(self, facets_dict, package_type):
        # keep existing facets, then add ours
        facets_dict['subject']              = toolkit._('Data Pillar')
        facets_dict['geologicalTimeframes'] = toolkit._('Geological Timeframe(s)')
        facets_dict['Regions']              = toolkit._('Region(s)')
        facets_dict['FeatureTypes']         = toolkit._('Feature Type(s)')
        return facets_dict
