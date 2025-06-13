# aps-kiota-python-demo

Experimental Python project using [Microsoft Kiota](https://learn.microsoft.com/en-us/openapi/kiota/overview) to generate SDK for [Autodesk Platform Services](https://aps.autodesk.com) API.

## Development

### Prerequisites

- APS application credentials
- Python 3 (tested with version 3.13)
- Docker

### Setup

- Setup Python virtual env: `python3 -m venv .venv && source .venv/bin/activate`
- Install Python dependencies: `pip install -r requirements.txt`
- (Optional) regenerate APS SDK: `./gen_sdk.sh`

### Testing 2-Legged OAuth

- Set the following environment variables:
    - `APS_CLIENT_ID` - your APS application client ID
    - `APS_CLIENT_SECRET` - your APS application client secret
- Run the test script: `python src/test_2_legged_oauth.py`

### Testing 3-Legged OAuth

- Set the following environment variables:
    - `APS_ACCESS_TOKEN` - your APS access token (3-legged)
- Run the test script: `python src/test_3_legged_oauth.py`

## Troubleshooting

### Python __future__ imports

There's a bug in Kiota [#4600](https://github.com/microsoft/kiota/issues/4600) where in certain cases the auto-generated Python code includes `__future__` imports in the wrong place. If you run into this issue, please make sure you are using [Kiota 1.27](https://github.com/microsoft/kiota/releases/tag/v1.27.0) or later of Kiota.

### Incorrect defaults for dataclass fields

There's a bug in Kiota [#6350](https://github.com/microsoft/kiota/issues/6350) where in certain cases the auto-generated Python code uses `[]` as default value for a `@dataclass` field. For now this must be fixed manually by replacing `[]` with `field(default_factory=list)`. There is a PR [#6655](https://github.com/microsoft/kiota/pull/6655) addressing this issue and will be released in [Kiota 1.28](https://github.com/microsoft/kiota/milestone/43)

> The auto-generated code in this project has already been updated to fix this issue.