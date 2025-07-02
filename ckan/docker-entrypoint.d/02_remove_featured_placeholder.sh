#!/bin/bash
# Remove grey featured placeholder from CKAN home page

# Path to CKAN templates
# The CKAN code lives under $SRC_DIR/ckan. Templates are in the
# "ckan/templates" directory inside the package.
TEMPLATE_DIR="${SRC_DIR}/ckan/ckan/templates/home"

# Remove lines including the featured snippet reference

if [ -d "$TEMPLATE_DIR" ]; then
  grep -rl "snippets/featured.html" "$TEMPLATE_DIR" 2>/dev/null | while read -r file; do
    echo "[remove_featured] cleaning $file"
    sed -i '/snippets\/featured.html/d' "$file"
  done

  FEATURED_FILE="$TEMPLATE_DIR/snippets/featured.html"
  if [ -f "$FEATURED_FILE" ]; then
    echo "{# featured snippet removed #}" > "$FEATURED_FILE"
  fi
fi
