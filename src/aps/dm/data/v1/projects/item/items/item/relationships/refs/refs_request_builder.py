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
    from .........models.filter_direction import Filter_direction
    from .........models.filter_ref_type import Filter_refType
    from .........models.filter_type_version import Filter_type_version
    from .........models.refs400_error import Refs400Error
    from .........models.refs403_error import Refs403Error
    from .........models.refs404_error import Refs404Error
    from .........models.relationship_refs import RelationshipRefs
    from .........models.relationship_refs400_error import RelationshipRefs400Error
    from .........models.relationship_refs403_error import RelationshipRefs403Error
    from .........models.relationship_refs404_error import RelationshipRefs404Error
    from .........models.relationship_refs_payload import RelationshipRefsPayload

class RefsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/items/{item_id}/relationships/refs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RefsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/items/{item_id}/relationships/refs{?filter%5Bdirection%5D*,filter%5Bextension%2Etype%5D*,filter%5Bid%5D*,filter%5BrefType%5D*,filter%5Btype%5D*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RefsRequestBuilderGetQueryParameters]] = None) -> Optional[RelationshipRefs]:
        """
        Returns the custom relationships that are associated with the specified item. Custom relationships can be established between an item and other resources within the ``data`` domain service (folders, items, and versions).Each relationship is defined by the ID of the object at the other end of the relationship, together with type, specific reference meta including extension data.Callers will typically use a filter parameter to restrict the response to the custom relationship types (``filter[meta.refType]``) they are interested in.The response body will have an included array that contains the resources in the relationship, which is essentially what is returned by the [List Related Resources for an Item](/en/docs/data/v2/reference/http/projects-project_id-items-item_id-refs-GET/) operation.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RelationshipRefs]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.refs400_error import Refs400Error
        from .........models.refs403_error import Refs403Error
        from .........models.refs404_error import Refs404Error
        from .........models.relationship_refs400_error import RelationshipRefs400Error
        from .........models.relationship_refs403_error import RelationshipRefs403Error
        from .........models.relationship_refs404_error import RelationshipRefs404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": RelationshipRefs400Error,
            "403": RelationshipRefs403Error,
            "404": RelationshipRefs404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.relationship_refs import RelationshipRefs

        return await self.request_adapter.send_async(request_info, RelationshipRefs, error_mapping)
    
    async def post(self,body: RelationshipRefsPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Creates a custom relationship between an item and another resource within the data domain service (folder, item, or version).
        param body: An object that describes the custom relationship to be created.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .........models.refs400_error import Refs400Error
        from .........models.refs403_error import Refs403Error
        from .........models.refs404_error import Refs404Error
        from .........models.relationship_refs400_error import RelationshipRefs400Error
        from .........models.relationship_refs403_error import RelationshipRefs403Error
        from .........models.relationship_refs404_error import RelationshipRefs404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Refs400Error,
            "403": Refs403Error,
            "404": Refs404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RefsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the custom relationships that are associated with the specified item. Custom relationships can be established between an item and other resources within the ``data`` domain service (folders, items, and versions).Each relationship is defined by the ID of the object at the other end of the relationship, together with type, specific reference meta including extension data.Callers will typically use a filter parameter to restrict the response to the custom relationship types (``filter[meta.refType]``) they are interested in.The response body will have an included array that contains the resources in the relationship, which is essentially what is returned by the [List Related Resources for an Item](/en/docs/data/v2/reference/http/projects-project_id-items-item_id-refs-GET/) operation.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: RelationshipRefsPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a custom relationship between an item and another resource within the data domain service (folder, item, or version).
        param body: An object that describes the custom relationship to be created.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.set_content_from_parsable(self.request_adapter, "application/vnd.api+json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> RefsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RefsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RefsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RefsRequestBuilderGetQueryParameters():
        """
        Returns the custom relationships that are associated with the specified item. Custom relationships can be established between an item and other resources within the ``data`` domain service (folders, items, and versions).Each relationship is defined by the ID of the object at the other end of the relationship, together with type, specific reference meta including extension data.Callers will typically use a filter parameter to restrict the response to the custom relationship types (``filter[meta.refType]``) they are interested in.The response body will have an included array that contains the resources in the relationship, which is essentially what is returned by the [List Related Resources for an Item](/en/docs/data/v2/reference/http/projects-project_id-items-item_id-refs-GET/) operation.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "filterdirection":
                return "filter%5Bdirection%5D"
            if original_name == "filterextension_type":
                return "filter%5Bextension%2Etype%5D"
            if original_name == "filterid":
                return "filter%5Bid%5D"
            if original_name == "filterref_type":
                return "filter%5BrefType%5D"
            if original_name == "filtertype":
                return "filter%5Btype%5D"
            return original_name
        
        # Filter by the direction of the reference. Possible values: ``from`` and ``to``.
        filterdirection: Optional[Filter_direction] = None

        # Filter by the extension type. 
        filterextension_type: Optional[list[str]] = None

        # Filter by the ``id`` of the ``ref`` target.
        filterid: Optional[list[str]] = None

        # Filter by ``refType``. Possible values: ``derived``, ``dependencies``, ``auxiliary``, ``xrefs``, and ``includes``.
        filterref_type: Optional[Filter_refType] = None

        # Filter by the ``type`` of the ``ref`` target. Supported values include ``folders``, ``items``, and ``versions``.
        filtertype: list[Filter_type_version] = []

    
    @dataclass
    class RefsRequestBuilderGetRequestConfiguration(RequestConfiguration[RefsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RefsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

