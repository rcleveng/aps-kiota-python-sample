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
    from .details.details_request_builder import DetailsRequestBuilder
    from .objects.objects_request_builder import ObjectsRequestBuilder

class WithBucketKeyItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/buckets/{bucketKey}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithBucketKeyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/buckets/{bucketKey}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Deletes the specified bucket. Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error. The initial processing of a bucket deletion request can be time-consuming. So, we recommend only deleting buckets containing a few objects, like those typically used for acceptance testing and prototyping. **Note:** Bucket keys will not be immediately available for reuse. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the specified bucket. Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error. The initial processing of a bucket deletion request can be time-consuming. So, we recommend only deleting buckets containing a few objects, like those typically used for acceptance testing and prototyping. **Note:** Bucket keys will not be immediately available for reuse. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def with_url(self,raw_url: str) -> WithBucketKeyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithBucketKeyItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithBucketKeyItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def details(self) -> DetailsRequestBuilder:
        """
        The details property
        """
        from .details.details_request_builder import DetailsRequestBuilder

        return DetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def objects(self) -> ObjectsRequestBuilder:
        """
        The objects property
        """
        from .objects.objects_request_builder import ObjectsRequestBuilder

        return ObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithBucketKeyItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

