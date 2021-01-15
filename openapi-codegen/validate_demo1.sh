#!/bin/bash

SPEC="../demo1/specs/openapi-university.yml"

java -jar swagger-codegen-cli.jar validate -i $SPEC


