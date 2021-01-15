#!/bin/bash
set -e

set -o allexport
[[ -f .env ]] && source .env
set +o allexport

docker-compose -f docker-compose.yml up

