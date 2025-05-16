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
    from ........models.access import Access
    from ........models.create_object_signed import Create_object_signed
    from ........models.create_signed_resource import Create_signed_resource

class SignedRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signed
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SignedRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/buckets/{bucketKey}/objects/{objectKey}/signed{?access*,useCdn*}", path_parameters)
    
    async def post(self,body: Create_signed_resource, request_configuration: Optional[RequestConfiguration[SignedRequestBuilderPostQueryParameters]] = None) -> Optional[Create_object_signed]:
        """
        Generates a signed URL that can be used to download or upload an object within the specified expiration time. If the object the signed URL points to is deleted or expires before the signed URL expires, the signed URL will no longer be valid.In addition to this operation that generates OSS signed URLs, OSS provides operations to generate S3 signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.Only the application that owns the bucket containing the object can call this operation.
        param body: The request payload for a Generate OSS Signed URL operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Create_object_signed]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.create_object_signed import Create_object_signed

        return await self.request_adapter.send_async(request_info, Create_object_signed, None)
    
    def to_post_request_information(self,body: Create_signed_resource, request_configuration: Optional[RequestConfiguration[SignedRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Generates a signed URL that can be used to download or upload an object within the specified expiration time. If the object the signed URL points to is deleted or expires before the signed URL expires, the signed URL will no longer be valid.In addition to this operation that generates OSS signed URLs, OSS provides operations to generate S3 signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.Only the application that owns the bucket containing the object can call this operation.
        param body: The request payload for a Generate OSS Signed URL operation.
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
    
    def with_url(self,raw_url: str) -> SignedRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SignedRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SignedRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SignedRequestBuilderPostQueryParameters():
        """
        Generates a signed URL that can be used to download or upload an object within the specified expiration time. If the object the signed URL points to is deleted or expires before the signed URL expires, the signed URL will no longer be valid.In addition to this operation that generates OSS signed URLs, OSS provides operations to generate S3 signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.Only the application that owns the bucket containing the object can call this operation.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "use_cdn":
                return "useCdn"
            if original_name == "access":
                return "access"
            return original_name
        
        access: Optional[Access] = None

        # ``true`` : Returns a Cloudfront URL to the object instead of an Autodesk URL (one that points to a location on https://developer.api.autodesk.com). Applications can interact with the Cloudfront URL exactly like with any classic public resource in OSS. They can use GET requests to download objects or PUT requests to upload objects.``false`` : (Default) Returns an Autodesk URL (one that points to a location on https://developer.api.autodesk.com) to the object.
        use_cdn: Optional[bool] = None

    
    @dataclass
    class SignedRequestBuilderPostRequestConfiguration(RequestConfiguration[SignedRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

