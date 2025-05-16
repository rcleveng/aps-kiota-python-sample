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
    from .......models.project import Project
    from .......models.project400_error import Project400Error
    from .......models.project403_error import Project403Error
    from .......models.project404_error import Project404Error
    from .hub.hub_request_builder import HubRequestBuilder
    from .top_folders.top_folders_request_builder import TopFoldersRequestBuilder

class WithProject_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /project/v1/hubs/{hub_id}/projects/{project_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithProject_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/project/v1/hubs/{hub_id}/projects/{project_id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Project]:
        """
        Returns the specified project from within the specified hub.For BIM 360 Docs, a hub ID corresponds to a BIM 360 account ID. To convert a BIM 360 account ID to a hub ID, prefix the account ID with ``b.``. For example, an account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.Similarly, to convert a BIM 360 project ID to a Data Management project ID prefix the BIM 360 Project ID with ``b.``. For example, a project ID of ``c8b0c73d-3ae9`` translates to a project ID of ``b.c8b0c73d-3ae9``.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Project]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.project400_error import Project400Error
        from .......models.project403_error import Project403Error
        from .......models.project404_error import Project404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Project400Error,
            "403": Project403Error,
            "404": Project404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.project import Project

        return await self.request_adapter.send_async(request_info, Project, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the specified project from within the specified hub.For BIM 360 Docs, a hub ID corresponds to a BIM 360 account ID. To convert a BIM 360 account ID to a hub ID, prefix the account ID with ``b.``. For example, an account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.Similarly, to convert a BIM 360 project ID to a Data Management project ID prefix the BIM 360 Project ID with ``b.``. For example, a project ID of ``c8b0c73d-3ae9`` translates to a project ID of ``b.c8b0c73d-3ae9``.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithProject_ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithProject_ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithProject_ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def hub(self) -> HubRequestBuilder:
        """
        The hub property
        """
        from .hub.hub_request_builder import HubRequestBuilder

        return HubRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def top_folders(self) -> TopFoldersRequestBuilder:
        """
        The topFolders property
        """
        from .top_folders.top_folders_request_builder import TopFoldersRequestBuilder

        return TopFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithProject_ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

