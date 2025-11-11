FROM ckan/ckan-base:2.11.0

# Install any extensions needed by your CKAN instance
# See Dockerfile.dev for more details and examples

# Temporarily become root so pip can write into /usr/lib/python3.10/site-packages
USER root

# PDF-view
RUN pip install ckanext-pdfview 

### Scheming ###
COPY ckanext-scheming /usr/src/ckanext-scheming
RUN pip install -e /usr/src/ckanext-scheming

RUN pip install ckanext-geoview

COPY logos/* ${APP_DIR}/src/ckan/ckan/public/base/images/
RUN chmod -R 755 ${APP_DIR}/src/ckan/ckan/public/base/images/

# Copy your local plugin into the image
COPY ckanext-customfacets /usr/src/ckanext-customfacets

# Install it in “editable” mode so the entry-point is registered
RUN pip install -e /usr/src/ckanext-customfacets

# Copy and install HESCOR-theme plugin
COPY ckanext-hescortheme /usr/src/ckanext-hescortheme
RUN pip install -e /usr/src/ckanext-hescortheme

# Switch back to the ckan user
USER ckan

# Copy custom initialization scripts
COPY docker-entrypoint.d/* /docker-entrypoint.d/

# Apply any patches needed to CKAN core or any of the built extensions (not the
# runtime mounted ones)
COPY patches ${APP_DIR}/patches

RUN for d in $APP_DIR/patches/*; do \
        if [ -d $d ]; then \
            for f in `ls $d/*.patch | sort -g`; do \
                cd $SRC_DIR/`basename "$d"` && echo "$0: Applying patch $f to $SRC_DIR/`basename $d`"; patch -p1 < "$f" ; \
            done ; \
        fi ; \
    done
