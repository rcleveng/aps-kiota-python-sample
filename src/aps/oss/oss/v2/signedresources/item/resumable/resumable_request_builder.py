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
    from ......models.object_details import ObjectDetails
    from ......models.reason import Reason
    from .resumable_put_request_body import ResumablePutRequestBody

class ResumableRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/signedresources/{hash}/resumable
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ResumableRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/signedresources/{hash}/resumable", path_parameters)
    
    async def put(self,body: ResumablePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ObjectDetails]:
        """
        Performs a resumable upload using an OSS signed URL. Use this operation to upload an object in chunks.**Note:** The signed URL returned by [Generate OSS Signed URL](/en/docs/data/v2/reference/http/signedresources-:id-GET/) contains the ``hash`` as a URI parameter. 
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ObjectDetails]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.reason import Reason

        error_mapping: dict[str, type[ParsableFactory]] = {
            "409": Reason,
            "416": Reason,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.object_details import ObjectDetails

        return await self.request_adapter.send_async(request_info, ObjectDetails, error_mapping)
    
    def to_put_request_information(self,body: ResumablePutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Performs a resumable upload using an OSS signed URL. Use this operation to upload an object in chunks.**Note:** The signed URL returned by [Generate OSS Signed URL](/en/docs/data/v2/reference/http/signedresources-:id-GET/) contains the ``hash`` as a URI parameter. 
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, application/vnd.api+json")
        request_info.set_content_from_parsable(self.request_adapter, "application/x-www-form-urlencoded", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ResumableRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ResumableRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ResumableRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ResumableRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

