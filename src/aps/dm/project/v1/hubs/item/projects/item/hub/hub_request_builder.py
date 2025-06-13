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
    from ........models.hub import Hub
    from ........models.hub400_error import Hub400Error
    from ........models.hub403_error import Hub403Error
    from ........models.hub404_error import Hub404Error

class HubRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /project/v1/hubs/{hub_id}/projects/{project_id}/hub
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new HubRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/project/v1/hubs/{hub_id}/projects/{project_id}/hub", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Hub]:
        """
        Returns the hub that contains the project specified by the  ``project_id`` parameter.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Hub]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.hub400_error import Hub400Error
        from ........models.hub403_error import Hub403Error
        from ........models.hub404_error import Hub404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Hub400Error,
            "403": Hub403Error,
            "404": Hub404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.hub import Hub

        return await self.request_adapter.send_async(request_info, Hub, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the hub that contains the project specified by the  ``project_id`` parameter.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> HubRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: HubRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return HubRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class HubRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

