#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

printf "Enter your skills: "
read -r SKILL
if [[ -z "$SKILL" ]]; then
  echo "Error: skill cannot be blank." >&2
  exit 1
fi

printf "Your %s skill is in high demand in the IT industry.\n" "$SKILL"

read -rp 'Username: ' USR
if [[ -z "$USR" ]]; then
  echo "Error: username cannot be blank." >&2
  exit 1
fi

read -rsp 'Password: ' PASS
printf '\n'
if [[ -z "$PASS" ]]; then
  echo "Error: password cannot be blank." >&2
  exit 1
fi

printf "Login successful: welcome, %s!\n" "$USR"
