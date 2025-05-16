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
    from ......models.folder import Folder
    from ......models.folder400_error import Folder400Error
    from ......models.folder403_error import Folder403Error
    from ......models.folder404_error import Folder404Error
    from ......models.folder409_error import Folder409Error
    from ......models.folder423_error import Folder423Error
    from ......models.folder_payload import FolderPayload
    from .item.with_folder_item_request_builder import WithFolder_ItemRequestBuilder

class FoldersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/folders
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FoldersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/folders", path_parameters)
    
    def by_folder_id(self,folder_id: str) -> WithFolder_ItemRequestBuilder:
        """
        Gets an item from the ApiSdk.data.v1.projects.item.folders.item collection
        param folder_id: The unique identifier of a folder.
        Returns: WithFolder_ItemRequestBuilder
        """
        if folder_id is None:
            raise TypeError("folder_id cannot be null.")
        from .item.with_folder_item_request_builder import WithFolder_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["folder_id"] = folder_id
        return WithFolder_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: FolderPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Folder]:
        """
        Creates a new folder in the specified project. Use the ``parent`` attribute in the request body to specify where in the hierarchy the new folder should be located. Folders can be nested up to 25 levels deep.Use the `Modify a Folder </en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-PATCH/>`_ operation to delete and restore folders.Before you use the Data Management API to access BIM 360 Docs folders, provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param body: Describe the folder to be created.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Folder]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.folder400_error import Folder400Error
        from ......models.folder403_error import Folder403Error
        from ......models.folder404_error import Folder404Error
        from ......models.folder409_error import Folder409Error
        from ......models.folder423_error import Folder423Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Folder400Error,
            "403": Folder403Error,
            "404": Folder404Error,
            "409": Folder409Error,
            "423": Folder423Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.folder import Folder

        return await self.request_adapter.send_async(request_info, Folder, error_mapping)
    
    def to_post_request_information(self,body: FolderPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new folder in the specified project. Use the ``parent`` attribute in the request body to specify where in the hierarchy the new folder should be located. Folders can be nested up to 25 levels deep.Use the `Modify a Folder </en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-PATCH/>`_ operation to delete and restore folders.Before you use the Data Management API to access BIM 360 Docs folders, provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param body: Describe the folder to be created.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/vnd.api+json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> FoldersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FoldersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FoldersRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FoldersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

