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
    from ......models.projects import Projects
    from ......models.projects400_error import Projects400Error
    from ......models.projects401_error import Projects401Error
    from ......models.projects403_error import Projects403Error
    from ......models.projects404_error import Projects404Error
    from .item.with_project_item_request_builder import WithProject_ItemRequestBuilder

class ProjectsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /project/v1/hubs/{hub_id}/projects
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ProjectsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/project/v1/hubs/{hub_id}/projects{?filter%5Bextension%2Etype%5D*,filter%5Bid%5D*,page%5Blimit%5D*,page%5Bnumber%5D*}", path_parameters)
    
    def by_project_id(self,project_id: str) -> WithProject_ItemRequestBuilder:
        """
        Gets an item from the ApiSdk.project.v1.hubs.item.projects.item collection
        param project_id: The unique identifier of a project. For BIM 360 Docs and ACC Docs, a hub ID corresponds to an Account ID. To convert a BIM 360 or ACC Account ID to a hub ID, prefix the Account ID with ``b.``. For example, an Account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.Similarly, to convert an ACC or BIM 360 project ID to a Data Management project ID prefix the ACC or BIM 360 project ID with ``b.``. For example, a project ID of ``c8b0c73d-3ae9`` translates to a project ID of ``b.c8b0c73d-3ae9``.
        Returns: WithProject_ItemRequestBuilder
        """
        if project_id is None:
            raise TypeError("project_id cannot be null.")
        from .item.with_project_item_request_builder import WithProject_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["project_id"] = project_id
        return WithProject_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ProjectsRequestBuilderGetQueryParameters]] = None) -> Optional[Projects]:
        """
        Returns a collection of active projects within the specified hub. The returned projects can be Autodesk Construction Cloud (ACC), BIM 360, BIM 360 Team, Fusion Team, and A360 Personal projects. For BIM 360 and ACC projects a hub ID corresponds to an Account ID. To convert an Account ID to a hub ID, prefix the account ID with ``b.``. For example, a BIM 360 account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.Similarly, to convert a BIM 360 and ACC project IDs to  Data Management project IDs prefix the BIM 360 or ACC Project ID with ``b.``. For example, a project ID of ``c8b0c73d-3ae9`` translates to a project ID of ``b.c8b0c73d-3ae9``.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Projects]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.projects400_error import Projects400Error
        from ......models.projects401_error import Projects401Error
        from ......models.projects403_error import Projects403Error
        from ......models.projects404_error import Projects404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Projects400Error,
            "401": Projects401Error,
            "403": Projects403Error,
            "404": Projects404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.projects import Projects

        return await self.request_adapter.send_async(request_info, Projects, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ProjectsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a collection of active projects within the specified hub. The returned projects can be Autodesk Construction Cloud (ACC), BIM 360, BIM 360 Team, Fusion Team, and A360 Personal projects. For BIM 360 and ACC projects a hub ID corresponds to an Account ID. To convert an Account ID to a hub ID, prefix the account ID with ``b.``. For example, a BIM 360 account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.Similarly, to convert a BIM 360 and ACC project IDs to  Data Management project IDs prefix the BIM 360 or ACC Project ID with ``b.``. For example, a project ID of ``c8b0c73d-3ae9`` translates to a project ID of ``b.c8b0c73d-3ae9``.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ProjectsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ProjectsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ProjectsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ProjectsRequestBuilderGetQueryParameters():
        """
        Returns a collection of active projects within the specified hub. The returned projects can be Autodesk Construction Cloud (ACC), BIM 360, BIM 360 Team, Fusion Team, and A360 Personal projects. For BIM 360 and ACC projects a hub ID corresponds to an Account ID. To convert an Account ID to a hub ID, prefix the account ID with ``b.``. For example, a BIM 360 account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.Similarly, to convert a BIM 360 and ACC project IDs to  Data Management project IDs prefix the BIM 360 or ACC Project ID with ``b.``. For example, a project ID of ``c8b0c73d-3ae9`` translates to a project ID of ``b.c8b0c73d-3ae9``.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
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
            if original_name == "pagelimit":
                return "page%5Blimit%5D"
            if original_name == "pagenumber":
                return "page%5Bnumber%5D"
            return original_name
        
        # Filter by the extension type. 
        filterextension_type: Optional[list[str]] = None

        # Filter by the ``id`` of the ``ref`` target.
        filterid: Optional[list[str]] = None

        # Specifies the maximum number of elements to return in the page. The default value is 200. The min value is 1. The max value is 200.
        pagelimit: Optional[int] = None

        # Specifies what page to return. Page numbers are 0-based (the first page is page 0).
        pagenumber: Optional[int] = None

    
    @dataclass
    class ProjectsRequestBuilderGetRequestConfiguration(RequestConfiguration[ProjectsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

