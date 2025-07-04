#!/bin/bash
set -e

if [ -z "$CKAN_SOLR_URL" ]; then
  echo "CKAN_SOLR_URL not set, skipping Solr schema update"
  exit 0
fi

SCHEMA_URL="${CKAN_SOLR_URL%/}/schema"
CORE_NAME=$(basename "$CKAN_SOLR_URL")

# Add field via Schema API (ignore errors if exists)
curl -s -H 'Content-Type: application/json' -X POST \
  --data-binary '{"add-field":{"name":"geologicalTimeframe","type":"string","multiValued":true,"stored":true,"indexed":true}}' \
  "$SCHEMA_URL" || true

# Reload core so new field takes effect
curl -s "${CKAN_SOLR_URL%/$CORE_NAME}/admin/cores?action=RELOAD&core=$CORE_NAME" >/dev/null || true
