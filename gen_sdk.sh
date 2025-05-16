#!/usr/bin/env bash

KIOTA_IMAGE="mcr.microsoft.com/openapi/kiota:1.26.1"
KIOTA_ARGS="--language python"
OPENAPI_BASE_URL="https://raw.githubusercontent.com/autodesk-platform-services/aps-sdk-openapi/09dfeb71fab0daf032cf1b343ef3dcac8ba1800c"

generate_sdk() {
    local output_dir="$1"
    local openapi_path="$2"
    local class_name="$3"
    docker run --volume "$output_dir":/app/output $KIOTA_IMAGE generate $KIOTA_ARGS --openapi "$OPENAPI_BASE_URL/$openapi_path" --class-name "$class_name"
}

generate_sdk "./src/aps/oss"        "oss/oss.yaml"                          "OssClient"
generate_sdk "./src/aps/md"         "modelderivative/modelderivative.yaml"  "ModelDerivativeClient"
generate_sdk "./src/aps/dm"         "datamanagement/datamanagement.yaml"    "DataManagementClient"
generate_sdk "./src/aps/acc/issues" "construction/issues/Issues.yaml"       "IssuesClient"