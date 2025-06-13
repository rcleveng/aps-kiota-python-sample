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
    from .......models.folder import Folder
    from .......models.folder400_error import Folder400Error
    from .......models.folder403_error import Folder403Error
    from .......models.folder404_error import Folder404Error
    from .......models.folder423_error import Folder423Error
    from .......models.modify_folder_payload import ModifyFolderPayload
    from .contents.contents_request_builder import ContentsRequestBuilder
    from .parent.parent_request_builder import ParentRequestBuilder
    from .refs.refs_request_builder import RefsRequestBuilder
    from .relationships.relationships_request_builder import RelationshipsRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder

class WithFolder_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/folders/{folder_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithFolder_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/folders/{folder_id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Folder]:
        """
        Returns the folder specified by the ``folder_id`` parameter from within the project identified by the ``project_id`` parameter. All folders and subfolders within a project (including the root folder) have a unique ID.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Folder]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.folder400_error import Folder400Error
        from .......models.folder403_error import Folder403Error
        from .......models.folder404_error import Folder404Error
        from .......models.folder423_error import Folder423Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Folder400Error,
            "403": Folder403Error,
            "404": Folder404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.folder import Folder

        return await self.request_adapter.send_async(request_info, Folder, error_mapping)
    
    async def patch(self,body: ModifyFolderPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Folder]:
        """
        Renames, moves, hides, or unhides a folder. Marking a BIM 360 Docs folder as hidden effectively deletes it. You can restore it by changing its ``hidden`` attribute. You can also move BIM 360 Docs folders by changing their parent folder.You cannot permanently delete BIM 360 Docs folders. They are tagged as hidden folders and are removed from the BIM 360 Docs UI and from regular Data Management API responses. You can use the hidden filter (``filter[hidden]=true``) to get a list of deleted folders with the [List Folder Contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET/) operation.Before you use the Data Management API to access BIM 360 Docs folders, provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](/en.docs.acc.v1/overview/introduction/). 
        param body: Modifies folder names
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Folder]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.folder400_error import Folder400Error
        from .......models.folder403_error import Folder403Error
        from .......models.folder404_error import Folder404Error
        from .......models.folder423_error import Folder423Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Folder400Error,
            "403": Folder403Error,
            "404": Folder404Error,
            "423": Folder423Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.folder import Folder

        return await self.request_adapter.send_async(request_info, Folder, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the folder specified by the ``folder_id`` parameter from within the project identified by the ``project_id`` parameter. All folders and subfolders within a project (including the root folder) have a unique ID.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ModifyFolderPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Renames, moves, hides, or unhides a folder. Marking a BIM 360 Docs folder as hidden effectively deletes it. You can restore it by changing its ``hidden`` attribute. You can also move BIM 360 Docs folders by changing their parent folder.You cannot permanently delete BIM 360 Docs folders. They are tagged as hidden folders and are removed from the BIM 360 Docs UI and from regular Data Management API responses. You can use the hidden filter (``filter[hidden]=true``) to get a list of deleted folders with the [List Folder Contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET/) operation.Before you use the Data Management API to access BIM 360 Docs folders, provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](/en.docs.acc.v1/overview/introduction/). 
        param body: Modifies folder names
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
    
    def with_url(self,raw_url: str) -> WithFolder_ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithFolder_ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithFolder_ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def contents(self) -> ContentsRequestBuilder:
        """
        The contents property
        """
        from .contents.contents_request_builder import ContentsRequestBuilder

        return ContentsRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def search(self) -> SearchRequestBuilder:
        """
        The search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithFolder_ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithFolder_ItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

