#!/bin/bash

# via https://github.com/swagger-api/swagger-codegen#prerequisites
wget wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.18/swagger-codegen-cli-2.4.18.jar -O swagger-codegen-cli.jar

v=`java -jar swagger-codegen-cli.jar version`

echo "Downloaded swagger codegen $v!"
echo "USAGE: java -jar swagger-codegen-cli.jar help"
