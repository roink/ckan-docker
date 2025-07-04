import os

from ckan.plugins import (
    implements,
    SingletonPlugin,
    IConfigurer,
    ITemplateHelpers
)
import ckan.plugins.toolkit as toolkit

class HescorTheme(SingletonPlugin):
    # Declare which plugin interfaces we implement
    implements(IConfigurer)
    implements(ITemplateHelpers)

    def update_config(self, config):
        """
        Called during CKAN startup. This is where we tell CKAN
        about our extension’s static files and Jinja templates.
        """
        here = os.path.dirname(__file__)

        # 1) Serve our CSS/JS/images from public/
        public_dir = os.path.join(here, 'public')
        toolkit.add_public_directory(config, public_dir)

        # 2) Serve our template overrides from templates/
        templates_dir = os.path.join(here, 'templates')
        toolkit.add_template_directory(config, templates_dir)

    def get_helpers(self):
        return {
            # if you have custom Jinja helpers, list them here
        }

