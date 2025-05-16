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
    from .......models.object_tree import ObjectTree
    from .properties.properties_request_builder import PropertiesRequestBuilder
    from .properties_query.properties_query_request_builder import PropertiesQueryRequestBuilder

class WithModelGuItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithModelGuItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata/{urn}/metadata/{modelGuid}{?forceget*,level*,objectid*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithModelGuItemRequestBuilderGetQueryParameters]] = None) -> Optional[ObjectTree]:
        """
        Retrieves the structured hierarchy of objects, known as an object tree, from the specified Model View (Viewable) within the specified source design. The object tree represents the arrangement and relationships of various objects present in that Model View.**Note:** A design file must be translated to SVF or SVF2 before you can retrieve its object tree.  Before you call this operation:- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views in the source design.- Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid``  parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ObjectTree]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.object_tree import ObjectTree

        return await self.request_adapter.send_async(request_info, ObjectTree, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithModelGuItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieves the structured hierarchy of objects, known as an object tree, from the specified Model View (Viewable) within the specified source design. The object tree represents the arrangement and relationships of various objects present in that Model View.**Note:** A design file must be translated to SVF or SVF2 before you can retrieve its object tree.  Before you call this operation:- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views in the source design.- Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid``  parameter.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithModelGuItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithModelGuItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithModelGuItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def properties(self) -> PropertiesRequestBuilder:
        """
        The properties property
        """
        from .properties.properties_request_builder import PropertiesRequestBuilder

        return PropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def properties_query(self) -> PropertiesQueryRequestBuilder:
        """
        The propertiesQuery property
        """
        from .properties_query.properties_query_request_builder import PropertiesQueryRequestBuilder

        return PropertiesQueryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithModelGuItemRequestBuilderGetQueryParameters():
        """
        Retrieves the structured hierarchy of objects, known as an object tree, from the specified Model View (Viewable) within the specified source design. The object tree represents the arrangement and relationships of various objects present in that Model View.**Note:** A design file must be translated to SVF or SVF2 before you can retrieve its object tree.  Before you call this operation:- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views in the source design.- Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid``  parameter.
        """
        # ``true``: Retrieves large resources, even beyond the 20 MB limit. If exceptionally large (over 800 MB), the system acts as if ``forceget`` is ``false``. ``false``: (Default) Does not retrieve resources if they are larger than 20 MB.
        forceget: Optional[str] = None

        # Specifies how many child levels of the hierarchy to return, when the ``objectid``  parameter is specified. Currently supports only ``level`` = ``1``.
        level: Optional[str] = None

        # If specified, retrieves the sub-tree that has the specified Object ID as its parent node. If this parameter is not specified, retrieves the entire object tree.
        objectid: Optional[int] = None

    
    @dataclass
    class WithModelGuItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithModelGuItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

