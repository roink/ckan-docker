# -*- coding: utf-8 -*-
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class CustomFacetsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IFacets)

    def dataset_facets(self, facets_dict, package_type):
        # keep existing facets, then add ours
        facets_dict['subject']              = toolkit._('Data Pillar')
        return facets_dict

    # CKAN will also call these when rendering group or organization pages.
    # Reuse the dataset facets so the same set appears everywhere.
    def organization_facets(self, facets_dict, organization_type, package_type):
        return self.dataset_facets(facets_dict, package_type)

    def group_facets(self, facets_dict, group_type, package_type):
        return self.dataset_facets(facets_dict, package_type)
