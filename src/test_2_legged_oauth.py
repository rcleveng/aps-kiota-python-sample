import asyncio
import base64
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from aps import OssClient, ModelDerivativeClient, ClientCredentialsAuthenticationProvider

# Assuming APS_CLIENT_ID and APS_CLIENT_SECRET are set in environment variables
adapter = HttpxRequestAdapter(ClientCredentialsAuthenticationProvider(scopes="bucket:read data:read"))
oss_client = OssClient(adapter)
model_derivative_client = ModelDerivativeClient(adapter)

async def get_buckets():
    try:
        response = await oss_client.oss.v2.buckets.get()
        buckets = response.items if response and response.items else []
        while response and response.next:
            response = await oss_client.oss.v2.buckets.with_url(response.next).get()
            buckets.extend(response.items if response and response.items else [])
        return buckets
    except Exception as e:
        print(f"Error fetching buckets: {e}")
        return []

async def get_objects(bucket_key: str):
    try:
        response = await oss_client.oss.v2.buckets.by_bucket_key(bucket_key).objects.get()
        objects = response.items if response and response.items else []
        while response and response.next:
            response = await oss_client.oss.v2.buckets.by_bucket_key(bucket_key).objects.with_url(response.next).get()
            objects.extend(response.items if response and response.items else [])
        return objects
    except Exception as e:
        print(f"Error fetching objects for bucket {bucket_key}: {e}")
        return []

async def get_viewables(object_id: str):
    urn = base64.urlsafe_b64encode(object_id.encode()).decode().rstrip('=')
    try:
        response = await model_derivative_client.modelderivative.v2.designdata.by_urn(urn).metadata.get()
        return response.data.metadata if response and response.data and response.data.metadata else []
    except Exception as e:
        print(f"Error fetching viewables for object {object_id}: {e}")
        return []

async def main():
    buckets = await get_buckets()
    for bucket in buckets:
        assert bucket.bucket_key
        print(f"Bucket: {bucket.bucket_key}")
        objects = await get_objects(bucket.bucket_key)
        for obj in objects:
            assert obj.object_id
            assert obj.object_key
            print(f"  Object: {obj.object_key}")
            viewables = await get_viewables(obj.object_id)
            for viewable in viewables:
                print(f"    Viewable: {viewable.name} ({viewable.guid})")

asyncio.run(main())