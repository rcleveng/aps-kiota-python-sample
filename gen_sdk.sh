#!/usr/bin/env bash

KIOTA_IMAGE="mcr.microsoft.com/openapi/kiota:1.26.1"
KIOTA_ARGS="--language python"

docker run --volume ./src/aps/oss:/app/output \
    $KIOTA_IMAGE generate $KIOTA_ARGS \
        --openapi https://raw.githubusercontent.com/autodesk-platform-services/aps-sdk-openapi/refs/heads/main/oss/oss.yaml \
        --class-name OssClient

docker run --volume ./src/aps/md:/app/output \
    $KIOTA_IMAGE generate $KIOTA_ARGS \
        --openapi https://raw.githubusercontent.com/autodesk-platform-services/aps-sdk-openapi/refs/heads/main/modelderivative/modelderivative.yaml \
        --class-name ModelDerivativeClient

docker run --volume ./src/aps/dm:/app/output \
    $KIOTA_IMAGE generate $KIOTA_ARGS \
        --openapi https://raw.githubusercontent.com/autodesk-platform-services/aps-sdk-openapi/refs/heads/main/datamanagement/datamanagement.yaml \
        --class-name DataManagementClient

docker run --volume ./src/aps/acc/issues:/app/output \
    $KIOTA_IMAGE generate $KIOTA_ARGS \
        --openapi https://raw.githubusercontent.com/autodesk-platform-services/aps-sdk-openapi/refs/heads/main/construction/issues/Issues.yaml \
        --class-name IssuesClient