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
    from ........models.top_folders import TopFolders
    from ........models.top_folders400_error import TopFolders400Error
    from ........models.top_folders403_error import TopFolders403Error
    from ........models.top_folders404_error import TopFolders404Error

class TopFoldersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /project/v1/hubs/{hub_id}/projects/{project_id}/topFolders
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TopFoldersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/project/v1/hubs/{hub_id}/projects/{project_id}/topFolders{?excludeDeleted*,projectFilesOnly*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TopFoldersRequestBuilderGetQueryParameters]] = None) -> Optional[TopFolders]:
        """
        Returns the details of the highest level folders within a project that the user calling this operation has access to. The user must have at least read access to the folders.If the user is a Project Admin, it returns all top-level folders in the project. Otherwise, it returns all the highest level folders in the folder hierarchy the user has access to.Users with access permission to a folder has access permission to all its subfolders.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TopFolders]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.top_folders400_error import TopFolders400Error
        from ........models.top_folders403_error import TopFolders403Error
        from ........models.top_folders404_error import TopFolders404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": TopFolders400Error,
            "403": TopFolders403Error,
            "404": TopFolders404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.top_folders import TopFolders

        return await self.request_adapter.send_async(request_info, TopFolders, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TopFoldersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the details of the highest level folders within a project that the user calling this operation has access to. The user must have at least read access to the folders.If the user is a Project Admin, it returns all top-level folders in the project. Otherwise, it returns all the highest level folders in the folder hierarchy the user has access to.Users with access permission to a folder has access permission to all its subfolders.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TopFoldersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TopFoldersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TopFoldersRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TopFoldersRequestBuilderGetQueryParameters():
        """
        Returns the details of the highest level folders within a project that the user calling this operation has access to. The user must have at least read access to the folders.If the user is a Project Admin, it returns all top-level folders in the project. Otherwise, it returns all the highest level folders in the folder hierarchy the user has access to.Users with access permission to a folder has access permission to all its subfolders.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "exclude_deleted":
                return "excludeDeleted"
            if original_name == "project_files_only":
                return "projectFilesOnly"
            return original_name
        
        # Specifies whether deleted folders are excluded from the response for BIM 360 Docs projects, when user context is provided. - ``true``: Response excludes deleted folders for BIM 360 Docs projects.  - ``false``: (Default) Response will not exclude deleted folders for BIM 360 Docs projects.
        exclude_deleted: Optional[bool] = None

        # Specifies what folders and subfolders to return for BIM 360 Docs projects, when user context is provided. - ``true``: Response will be restricted to folder and subfolders containing project files for BIM 360 Docs projects.  - ``false``: (Default) Response will include all available folders.
        project_files_only: Optional[bool] = None

    
    @dataclass
    class TopFoldersRequestBuilderGetRequestConfiguration(RequestConfiguration[TopFoldersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

