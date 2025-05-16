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

There's a bug in Kiota [#4600](https://github.com/microsoft/kiota/issues/4600) where in certain cases the auto-generated Python code includes `__future__` imports in the wrong place. For now this must be fixed manually by moving the `from __future__ import annotations` line to the top of the file.

> The auto-generated code in this project has already been updated to fix this issue.

### Incorrect defaults for dataclass fields

There's a bug in Kiota [#6350](https://github.com/microsoft/kiota/issues/6350) where in certain cases the auto-generated Python code uses `[]` as default value for a `@dataclass` field. For now this must be fixed manually by replacing `[]` with `field(default_factory=list)`. There is a PR [#6489](https://github.com/microsoft/kiota/pull/6489) addressing this issue, waiting to be merged.

> The auto-generated code in this project has already been updated to fix this issue.