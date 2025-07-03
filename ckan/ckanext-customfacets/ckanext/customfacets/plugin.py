# -*- coding: utf-8 -*-
import json
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class CustomFacetsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController, inherit=True)

    def dataset_facets(self, facets_dict, package_type):
        # keep existing facets, then add ours
        facets_dict['subject']              = toolkit._('Data Pillar')
        facets_dict['language']             = toolkit._('Language')
        facets_dict['keywords']             = toolkit._('Keywords')
        facets_dict['rights']             = toolkit._('License')
        facets_dict['format']             = toolkit._('File Type')
        facets_dict['geologicalTimeframe'] = toolkit._('Geological Timeframe')
        return facets_dict

    # CKAN will also call these when rendering group or organization pages.
    # Reuse the dataset facets so the same set appears everywhere.
    def organization_facets(self, facets_dict, organization_type, package_type):
        return self.dataset_facets(facets_dict, package_type)

    def group_facets(self, facets_dict, group_type, package_type):
        return self.dataset_facets(facets_dict, package_type)

    def before_index(self, data_dict):
        """Extract geological timeframe values for faceting."""
        # Values might already be a list or a JSON string
        raw = data_dict.get('geologicalTimeframes')

        if not raw:
            # Look for the extras entry if the field is stored there
            for extra in data_dict.get('extras', []):
                if extra.get('key') == 'geologicalTimeframes':
                    raw = extra.get('value')
                    break

        if isinstance(raw, str):
            try:
                raw = json.loads(raw)
            except Exception:
                raw = []

        values = []
        if isinstance(raw, list):
            for entry in raw:
                if isinstance(entry, dict):
                    tf = entry.get('geologicalTimeframe')
                    if tf:
                        values.append(tf)

        if values:
            data_dict['geologicalTimeframe'] = values

        return data_dict
