#!/bin/bash

SPEC="../demo1/specs/openapi-university.yml"
OUTDIR="../demo1/client_python"


# via https://github.com/swagger-api/swagger-codegen#generators

java -jar swagger-codegen-cli.jar generate \
  -i $SPEC \
  -l python \
  -o $OUTDIR

