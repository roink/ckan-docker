FROM ckan/ckan-base:2.11.0

# Install any extensions needed by your CKAN instance
# See Dockerfile.dev for more details and examples

# PDF-view
RUN pip install ckanext-pdfview 

### Scheming ###
RUN pip install -e 'git+https://github.com/roink/ckanext-scheming.git@master#egg=ckanext-scheming'

RUN pip install ckanext-geoview

# Copy custom initialization scripts
COPY docker-entrypoint.d/* /docker-entrypoint.d/

# Apply any patches needed to CKAN core or any of the built extensions (not the
# runtime mounted ones)
COPY patches ${APP_DIR}/patches

COPY logos/* ${APP_DIR}/src/ckan/ckan/public/base/images/
RUN chmod -R 755 ${APP_DIR}/src/ckan/ckan/public/base/images/

RUN for d in $APP_DIR/patches/*; do \
        if [ -d $d ]; then \
            for f in `ls $d/*.patch | sort -g`; do \
                cd $SRC_DIR/`basename "$d"` && echo "$0: Applying patch $f to $SRC_DIR/`basename $d`"; patch -p1 < "$f" ; \
            done ; \
        fi ; \
    done
