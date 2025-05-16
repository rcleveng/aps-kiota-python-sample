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
    from .......models.batchsigneds3download_object import Batchsigneds3download_object
    from .......models.batchsigneds3download_response import Batchsigneds3download_response

class Batchsigneds3downloadRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/buckets/{bucketKey}/objects/batchsigneds3download
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new Batchsigneds3downloadRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/buckets/{bucketKey}/objects/batchsigneds3download{?minutesExpiration*,public%2Dresource%2Dfallback*}", path_parameters)
    
    async def post(self,body: Batchsigneds3download_object, request_configuration: Optional[RequestConfiguration[Batchsigneds3downloadRequestBuilderPostQueryParameters]] = None) -> Optional[Batchsigneds3download_response]:
        """
        Creates and returns signed URLs to download a set of objects directly from S3. These signed URLs expire in 2 minutes by default, but you can change this duration if needed.  You must start download the objects before the signed URLs expire. The download itself can take longer.Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.
        param body: The response to a Batch Generate Signed S3 Download URLs operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Batchsigneds3download_response]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.batchsigneds3download_response import Batchsigneds3download_response

        return await self.request_adapter.send_async(request_info, Batchsigneds3download_response, None)
    
    def to_post_request_information(self,body: Batchsigneds3download_object, request_configuration: Optional[RequestConfiguration[Batchsigneds3downloadRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates and returns signed URLs to download a set of objects directly from S3. These signed URLs expire in 2 minutes by default, but you can change this duration if needed.  You must start download the objects before the signed URLs expire. The download itself can take longer.Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.
        param body: The response to a Batch Generate Signed S3 Download URLs operation.
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
    
    def with_url(self,raw_url: str) -> Batchsigneds3downloadRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Batchsigneds3downloadRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return Batchsigneds3downloadRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class Batchsigneds3downloadRequestBuilderPostQueryParameters():
        """
        Creates and returns signed URLs to download a set of objects directly from S3. These signed URLs expire in 2 minutes by default, but you can change this duration if needed.  You must start download the objects before the signed URLs expire. The download itself can take longer.Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.
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
            return original_name
        
        # The time window (in minutes) the signed URL will remain usable. Acceptable values = 1-60 minutes. Default = 2 minutes.**Tip:** Use the smallest possible time window to minimize exposure of the signed URL.
        minutes_expiration: Optional[int] = None

        # Specifies how to return the signed URLs, in case the object was uploaded in chunks, and assembling of chunks is not yet complete.- ``true`` : Return a single signed OSS URL.- ``false`` : (Default) Return multiple signed S3 URLs, where each URL points to a chunk.
        public_resource_fallback: Optional[bool] = None

    
    @dataclass
    class Batchsigneds3downloadRequestBuilderPostRequestConfiguration(RequestConfiguration[Batchsigneds3downloadRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

