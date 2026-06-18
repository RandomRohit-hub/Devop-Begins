#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

readonly PACKAGE_LIST=(wget unzip httpd)
readonly TEMP_DIR="/tmp/webfiles"
readonly WEB_ARTIFACT_URL="https://www.tooplate.com/zip-templates/2098_health.zip"
readonly WEB_CONTENT_DIR="2098_health"
readonly WEB_ROOT="/var/www/html"

cleanup() {
  rm -rf "${TEMP_DIR}"
}
trap cleanup EXIT

log() {
  echo "########################################"
  echo "$1"
  echo "########################################"
}

log "Installing packages."
sudo yum install -y "${PACKAGE_LIST[@]}" > /dev/null

gitignore=""
log "Starting HTTPD service."
sudo systemctl start httpd
sudo systemctl enable httpd

log "Starting artifact deployment."
mkdir -p "${TEMP_DIR}"
cd "${TEMP_DIR}" || exit 1

wget -q "${WEB_ARTIFACT_URL}"
unzip -q "${WEB_CONTENT_DIR}.zip"
sudo cp -r "${WEB_CONTENT_DIR}"/* "${WEB_ROOT}/"

log "Restarting HTTPD service."
sudo systemctl restart httpd

log "Deployment complete."
sudo systemctl status httpd --no-pager
ls "${WEB_ROOT}"



