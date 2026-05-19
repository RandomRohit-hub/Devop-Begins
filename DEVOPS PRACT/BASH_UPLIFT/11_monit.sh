#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

SERVICE_NAME="httpd"
BANNER="#####################################################"

function log() {
  printf "%s\n" "$1"
}

function is_service_running() {
  if command -v systemctl >/dev/null 2>&1; then
    systemctl is-active --quiet "$SERVICE_NAME"
  else
    pidof "$SERVICE_NAME" >/dev/null 2>&1
  fi
}

function start_service() {
  if command -v systemctl >/dev/null 2>&1; then
    systemctl start "$SERVICE_NAME"
  else
    service "$SERVICE_NAME" start
  fi
}

log "$BANNER"
date

if is_service_running; then
  log "${SERVICE_NAME^} is running."
else
  log "${SERVICE_NAME^} is NOT running."
  log "Attempting to start ${SERVICE_NAME}..."

  if start_service; then
    log "${SERVICE_NAME^} started successfully."
  else
    log "Failed to start ${SERVICE_NAME}. Contact the administrator."
    exit 1
  fi
fi

log "$BANNER"
log ""
