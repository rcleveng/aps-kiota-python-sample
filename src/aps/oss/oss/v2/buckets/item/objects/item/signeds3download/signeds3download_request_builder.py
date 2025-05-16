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
    from ........models.signeds3download_response import Signeds3download_response

class Signeds3downloadRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3download
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new Signeds3downloadRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3download{?minutesExpiration*,public%2Dresource%2Dfallback*,response%2Dcache%2Dcontrol*,response%2Dcontent%2Ddisposition*,response%2Dcontent%2Dtype*,useCdn*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[Signeds3downloadRequestBuilderGetQueryParameters]] = None) -> Optional[Signeds3download_response]:
        """
        Gets a signed URL to download an object directly from S3, bypassing OSS servers. This signed URL expires in 2 minutes by default, but you can change this duration if needed.  You must start the download before the signed URL expires. The download itself can take longer. If the download fails after the validity period of the signed URL has elapsed, you can call this operation again to obtain a fresh signed URL.Only applications that have read access to the object can call this operation.   You can use range headers with the signed download URL to download the object in chunks. This ability lets you download chunks in parallel, which can result in faster downloads.If the object you want to download was uploaded in chunks and is still assembling on OSS, you will receive multiple S3 URLs instead of just one. Each URL will point to a chunk. If you prefer to receive a single URL, set the ``public-resource-fallback`` query parameter to ``true``. This setting will make OSS fallback to returning a single signed OSS URL, if assembling is still in progress. In addition to this operation that generates S3 signed URLs, OSS provides an operation to generate OSS signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Signeds3download_response]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.signeds3download_response import Signeds3download_response

        return await self.request_adapter.send_async(request_info, Signeds3download_response, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[Signeds3downloadRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets a signed URL to download an object directly from S3, bypassing OSS servers. This signed URL expires in 2 minutes by default, but you can change this duration if needed.  You must start the download before the signed URL expires. The download itself can take longer. If the download fails after the validity period of the signed URL has elapsed, you can call this operation again to obtain a fresh signed URL.Only applications that have read access to the object can call this operation.   You can use range headers with the signed download URL to download the object in chunks. This ability lets you download chunks in parallel, which can result in faster downloads.If the object you want to download was uploaded in chunks and is still assembling on OSS, you will receive multiple S3 URLs instead of just one. Each URL will point to a chunk. If you prefer to receive a single URL, set the ``public-resource-fallback`` query parameter to ``true``. This setting will make OSS fallback to returning a single signed OSS URL, if assembling is still in progress. In addition to this operation that generates S3 signed URLs, OSS provides an operation to generate OSS signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> Signeds3downloadRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Signeds3downloadRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return Signeds3downloadRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class Signeds3downloadRequestBuilderGetQueryParameters():
        """
        Gets a signed URL to download an object directly from S3, bypassing OSS servers. This signed URL expires in 2 minutes by default, but you can change this duration if needed.  You must start the download before the signed URL expires. The download itself can take longer. If the download fails after the validity period of the signed URL has elapsed, you can call this operation again to obtain a fresh signed URL.Only applications that have read access to the object can call this operation.   You can use range headers with the signed download URL to download the object in chunks. This ability lets you download chunks in parallel, which can result in faster downloads.If the object you want to download was uploaded in chunks and is still assembling on OSS, you will receive multiple S3 URLs instead of just one. Each URL will point to a chunk. If you prefer to receive a single URL, set the ``public-resource-fallback`` query parameter to ``true``. This setting will make OSS fallback to returning a single signed OSS URL, if assembling is still in progress. In addition to this operation that generates S3 signed URLs, OSS provides an operation to generate OSS signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "minutes_expiration":
                return "minutesExpiration"
            if original_name == "public_resource_fallback":
                return "public%2Dresource%2Dfallback"
            if original_name == "response_cache_control":
                return "response%2Dcache%2Dcontrol"
            if original_name == "response_content_disposition":
                return "response%2Dcontent%2Ddisposition"
            if original_name == "response_content_type":
                return "response%2Dcontent%2Dtype"
            if original_name == "use_cdn":
                return "useCdn"
            return original_name
        
        # The time window (in minutes) the signed URL will remain usable. Acceptable values = 1-60 minutes. Default = 2 minutes.**Tip:** Use the smallest possible time window to minimize exposure of the signed URL.
        minutes_expiration: Optional[int] = None

        # Specifies how to return the signed URLs, in case the object was uploaded in chunks, and assembling of chunks is not yet complete.- ``true`` : Return a single signed OSS URL.- ``false`` : (Default) Return multiple signed S3 URLs, where each URL points to a chunk.
        public_resource_fallback: Optional[bool] = None

        # The value of the Cache-Control header you want to receive when you download the object using the signed URL. If you do not specify a value, the Cache-Control header defaults to the value stored with OSS.
        response_cache_control: Optional[str] = None

        # The value of the Content-Disposition header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Disposition header defaults to the value stored with OSS.
        response_content_disposition: Optional[str] = None

        # The value of the Content-Type header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Type header defaults to the value stored with OSS.
        response_content_type: Optional[str] = None

        # ``true`` : Returns a URL that points to a CloudFront edge location.``false`` : (Default) Returns a URL that points directly to the S3 object.
        use_cdn: Optional[bool] = None

    
    @dataclass
    class Signeds3downloadRequestBuilderGetRequestConfiguration(RequestConfiguration[Signeds3downloadRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

