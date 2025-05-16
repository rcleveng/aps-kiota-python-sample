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
    from .......models.item import Item
    from .......models.item400_error import Item400Error
    from .......models.item403_error import Item403Error
    from .......models.item404_error import Item404Error
    from .......models.item423_error import Item423Error
    from .......models.modify_item_payload import ModifyItemPayload
    from .parent.parent_request_builder import ParentRequestBuilder
    from .refs.refs_request_builder import RefsRequestBuilder
    from .relationships.relationships_request_builder import RelationshipsRequestBuilder
    from .tip.tip_request_builder import TipRequestBuilder
    from .versions.versions_request_builder import VersionsRequestBuilder

class WithItem_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/items/{item_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithItem_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/items/{item_id}{?includePathInProject*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithItem_ItemRequestBuilderGetQueryParameters]] = None) -> Optional[Item]:
        """
        Retrieves an item. Items represent Word documents, Fusion 360 design files, drawings, spreadsheets, etc.The tip version for the item is included in the included array of the payload.To retrieve multiple items, see the ListItems command.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Item]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.item400_error import Item400Error
        from .......models.item403_error import Item403Error
        from .......models.item404_error import Item404Error
        from .......models.item423_error import Item423Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Item400Error,
            "403": Item403Error,
            "404": Item404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.item import Item

        return await self.request_adapter.send_async(request_info, Item, error_mapping)
    
    async def patch(self,body: ModifyItemPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Item]:
        """
        Updates the ``displayName`` of the specified item. Note that updating the ``displayName`` of an item is not supported for BIM 360 Docs or ACC items.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param body: An object that defines the attributes of an item that must be updated.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Item]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.item400_error import Item400Error
        from .......models.item403_error import Item403Error
        from .......models.item404_error import Item404Error
        from .......models.item423_error import Item423Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Item400Error,
            "403": Item403Error,
            "404": Item404Error,
            "423": Item423Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.item import Item

        return await self.request_adapter.send_async(request_info, Item, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithItem_ItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieves an item. Items represent Word documents, Fusion 360 design files, drawings, spreadsheets, etc.The tip version for the item is included in the included array of the payload.To retrieve multiple items, see the ListItems command.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ModifyItemPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the ``displayName`` of the specified item. Note that updating the ``displayName`` of an item is not supported for BIM 360 Docs or ACC items.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param body: An object that defines the attributes of an item that must be updated.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/vnd.api+json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WithItem_ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithItem_ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithItem_ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def parent(self) -> ParentRequestBuilder:
        """
        The parent property
        """
        from .parent.parent_request_builder import ParentRequestBuilder

        return ParentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def refs(self) -> RefsRequestBuilder:
        """
        The refs property
        """
        from .refs.refs_request_builder import RefsRequestBuilder

        return RefsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def relationships(self) -> RelationshipsRequestBuilder:
        """
        The relationships property
        """
        from .relationships.relationships_request_builder import RelationshipsRequestBuilder

        return RelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tip(self) -> TipRequestBuilder:
        """
        The tip property
        """
        from .tip.tip_request_builder import TipRequestBuilder

        return TipRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> VersionsRequestBuilder:
        """
        The versions property
        """
        from .versions.versions_request_builder import VersionsRequestBuilder

        return VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithItem_ItemRequestBuilderGetQueryParameters():
        """
        Retrieves an item. Items represent Word documents, Fusion 360 design files, drawings, spreadsheets, etc.The tip version for the item is included in the included array of the payload.To retrieve multiple items, see the ListItems command.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_path_in_project":
                return "includePathInProject"
            return original_name
        
        # Specify whether to return ``pathInProject`` attribute in response for BIM 360 Docs projects. ``pathInProject`` is the relative path of the item starting from project’s root folder. - ``true``: Response will include the ``pathInProject`` attribute for BIM 360 Docs projects.  - ``false``: (Default) Response will not include ``pathInProject`` attribute for BIM 360 Docs projects.
        include_path_in_project: Optional[bool] = None

    
    @dataclass
    class WithItem_ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithItem_ItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithItem_ItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

