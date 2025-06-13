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
    from ........models.item_tip import ItemTip
    from ........models.item_tip400_error import ItemTip400Error
    from ........models.item_tip403_error import ItemTip403Error
    from ........models.item_tip404_error import ItemTip404Error

class TipRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/items/{item_id}/tip
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TipRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/items/{item_id}/tip", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ItemTip]:
        """
        Returns the latest version of the specified item. A project can contain multiple versions of a resource item. The latest version is referred to as the tip version, which is returned by this operation.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ItemTip]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.item_tip400_error import ItemTip400Error
        from ........models.item_tip403_error import ItemTip403Error
        from ........models.item_tip404_error import ItemTip404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ItemTip400Error,
            "403": ItemTip403Error,
            "404": ItemTip404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.item_tip import ItemTip

        return await self.request_adapter.send_async(request_info, ItemTip, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the latest version of the specified item. A project can contain multiple versions of a resource item. The latest version is referred to as the tip version, which is returned by this operation.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TipRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TipRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TipRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TipRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

