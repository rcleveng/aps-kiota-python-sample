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
    from ....models.hubs import Hubs
    from ....models.hubs401_error import Hubs401Error
    from ....models.hubs403_error import Hubs403Error
    from .item.with_hub_item_request_builder import WithHub_ItemRequestBuilder

class HubsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /project/v1/hubs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new HubsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/project/v1/hubs{?filter%5Bextension%2Etype%5D*,filter%5Bid%5D*,filter%5Bname%5D*}", path_parameters)
    
    def by_hub_id(self,hub_id: str) -> WithHub_ItemRequestBuilder:
        """
        Gets an item from the ApiSdk.project.v1.hubs.item collection
        param hub_id: The unique identifier of a hub.
        Returns: WithHub_ItemRequestBuilder
        """
        if hub_id is None:
            raise TypeError("hub_id cannot be null.")
        from .item.with_hub_item_request_builder import WithHub_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["hub_id"] = hub_id
        return WithHub_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[HubsRequestBuilderGetQueryParameters]] = None) -> Optional[Hubs]:
        """
        Returns a collection of hubs that the user of your app can access.The returned hubs can be BIM 360 Team hubs, Fusion Team hubs (formerly known as A360 Team hubs), A360 Personal hubs, ACC Docs (Autodesk Docs) accounts, or BIM 360 Docs accounts. Only active hubs are returned.For BIM 360 Docs and ACC Docs, a hub ID corresponds to an Account ID. To convert a BIM 360 or ACC Account ID to a hub ID, prefix the Account ID with ``b.``. For example, an Account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Hubs]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.hubs401_error import Hubs401Error
        from ....models.hubs403_error import Hubs403Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": Hubs401Error,
            "403": Hubs403Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.hubs import Hubs

        return await self.request_adapter.send_async(request_info, Hubs, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[HubsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a collection of hubs that the user of your app can access.The returned hubs can be BIM 360 Team hubs, Fusion Team hubs (formerly known as A360 Team hubs), A360 Personal hubs, ACC Docs (Autodesk Docs) accounts, or BIM 360 Docs accounts. Only active hubs are returned.For BIM 360 Docs and ACC Docs, a hub ID corresponds to an Account ID. To convert a BIM 360 or ACC Account ID to a hub ID, prefix the Account ID with ``b.``. For example, an Account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> HubsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: HubsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return HubsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class HubsRequestBuilderGetQueryParameters():
        """
        Returns a collection of hubs that the user of your app can access.The returned hubs can be BIM 360 Team hubs, Fusion Team hubs (formerly known as A360 Team hubs), A360 Personal hubs, ACC Docs (Autodesk Docs) accounts, or BIM 360 Docs accounts. Only active hubs are returned.For BIM 360 Docs and ACC Docs, a hub ID corresponds to an Account ID. To convert a BIM 360 or ACC Account ID to a hub ID, prefix the Account ID with ``b.``. For example, an Account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "filterextension_type":
                return "filter%5Bextension%2Etype%5D"
            if original_name == "filterid":
                return "filter%5Bid%5D"
            if original_name == "filtername":
                return "filter%5Bname%5D"
            return original_name
        
        # Filter by the extension type. 
        filterextension_type: Optional[list[str]] = None

        # Filter by the ``id`` of the ``ref`` target.
        filterid: Optional[list[str]] = None

        # Filter by the ``name`` of the ``ref`` target.
        filtername: Optional[list[str]] = None

    
    @dataclass
    class HubsRequestBuilderGetRequestConfiguration(RequestConfiguration[HubsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

