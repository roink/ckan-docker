#!/bin/bash
# Remove grey featured placeholder from CKAN home page

# Path to CKAN templates
TEMPLATE_DIR="${SRC_DIR}/ckan/templates/home"

# Remove lines including the featured snippet reference
if [ -d "$TEMPLATE_DIR" ]; then
  grep -rl "featured.html" "$TEMPLATE_DIR" 2>/dev/null | while read -r file; do
    echo "[remove_featured] cleaning $file"
    sed -i '/featured.html/d' "$file"
  done

  FEATURED_FILE="$TEMPLATE_DIR/snippets/featured.html"
  if [ -f "$FEATURED_FILE" ]; then
    echo "{# featured snippet removed #}" > "$FEATURED_FILE"
  fi
fi
