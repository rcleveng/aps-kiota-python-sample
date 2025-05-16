from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.bucket import Bucket
    from ....models.buckets import Buckets
    from ....models.create_buckets_payload import Create_buckets_payload
    from ....models.reason import Reason
    from ....models.region import Region
    from .item.with_bucket_key_item_request_builder import WithBucketKeyItemRequestBuilder

class BucketsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/buckets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BucketsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/buckets{?limit*,region*,startAt*}", path_parameters)
    
    def by_bucket_key(self,bucket_key: str) -> WithBucketKeyItemRequestBuilder:
        """
        Gets an item from the ApiSdk.oss.v2.buckets.item collection
        param bucket_key: The bucket key of the bucket to delete.
        Returns: WithBucketKeyItemRequestBuilder
        """
        if bucket_key is None:
            raise TypeError("bucket_key cannot be null.")
        from .item.with_bucket_key_item_request_builder import WithBucketKeyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bucketKey"] = bucket_key
        return WithBucketKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[BucketsRequestBuilderGetQueryParameters]] = None) -> Optional[Buckets]:
        """
        Returns a list of buckets owned by the application. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Buckets]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.buckets import Buckets

        return await self.request_adapter.send_async(request_info, Buckets, None)
    
    async def post(self,body: Create_buckets_payload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Bucket]:
        """
        Creates a bucket. Buckets are virtual container within the Object Storage Service (OSS), which you can use to store and manage objects (files) in the cloud. The application creating the bucket is the owner of the bucket.**Note:** Do not use this operation to create buckets for BIM360 Document Management. Use [POST projects/{project_id}/storage](/en/docs/data/v2/reference/http/projects-project_id-storage-POST>) instead. For details, see [Upload Files to BIM 360 Document Management](/en/docs/bim360/v1/tutorials/document-management/upload-document).
        param body: The request payload for the Create Bucket operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Bucket]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.reason import Reason

        error_mapping: dict[str, type[ParsableFactory]] = {
            "409": Reason,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.bucket import Bucket

        return await self.request_adapter.send_async(request_info, Bucket, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[BucketsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of buckets owned by the application. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, application/vnd.api+json")
        return request_info
    
    def to_post_request_information(self,body: Create_buckets_payload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a bucket. Buckets are virtual container within the Object Storage Service (OSS), which you can use to store and manage objects (files) in the cloud. The application creating the bucket is the owner of the bucket.**Note:** Do not use this operation to create buckets for BIM360 Document Management. Use [POST projects/{project_id}/storage](/en/docs/data/v2/reference/http/projects-project_id-storage-POST>) instead. For details, see [Upload Files to BIM 360 Document Management](/en/docs/bim360/v1/tutorials/document-management/upload-document).
        param body: The request payload for the Create Bucket operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, application/vnd.api+json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> BucketsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BucketsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BucketsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class BucketsRequestBuilderGetQueryParameters():
        """
        Returns a list of buckets owned by the application. 
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "start_at":
                return "startAt"
            if original_name == "limit":
                return "limit"
            if original_name == "region":
                return "region"
            return original_name
        
        # The number of items you want per page.Acceptable values = 1-100. Default = 10.
        limit: Optional[int] = None

        # Specifies where the bucket containing the object stored. Possible values are:- ``US`` - (Default) Data center for the US region.- ``EMEA`` - Data center for the European Union, Middle East, and Africa.- ``APAC`` -  (Beta) Data center for Australia.**Note:** Beta features are subject to change. Please do not use in production environments.
        region: Optional[Region] = None

        # The ID of the last item that was returned in the previous result set.  It enables the system to return subsequent items starting from the next one after the specified ID.
        start_at: Optional[str] = None

    
    @dataclass
    class BucketsRequestBuilderGetRequestConfiguration(RequestConfiguration[BucketsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BucketsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

