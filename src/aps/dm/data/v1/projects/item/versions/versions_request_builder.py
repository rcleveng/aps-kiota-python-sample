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
    from ......models.created_version import CreatedVersion
    from ......models.created_version400_error import CreatedVersion400Error
    from ......models.created_version403_error import CreatedVersion403Error
    from ......models.created_version404_error import CreatedVersion404Error
    from ......models.created_version423_error import CreatedVersion423Error
    from ......models.version_payload import VersionPayload
    from .item.with_version_item_request_builder import WithVersion_ItemRequestBuilder

class VersionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/versions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VersionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/versions{?copyFrom*}", path_parameters)
    
    def by_version_id(self,version_id: str) -> WithVersion_ItemRequestBuilder:
        """
        Gets an item from the ApiSdk.data.v1.projects.item.versions.item collection
        param version_id: The URL encoded unique identifier of a version.
        Returns: WithVersion_ItemRequestBuilder
        """
        if version_id is None:
            raise TypeError("version_id cannot be null.")
        from .item.with_version_item_request_builder import WithVersion_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["version_id"] = version_id
        return WithVersion_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: VersionPayload, request_configuration: Optional[RequestConfiguration[VersionsRequestBuilderPostQueryParameters]] = None) -> Optional[CreatedVersion]:
        """
        Creates a new versions of an existing item.Before creating a new version you must create a storage location for the version in OSS, and upload the file to that location. For more details about the workflow, see the tutorial on uploading a file.This operation also allows you to create a new version of an item by copying a specific version of an existing item from another folder within the project. The new version becomes the tip version of the item.Use the [Create an Item](/en/docs/data/v2/reference/http/projects-project_id-items-POST/) operation to copy a specific version of an existing item as a new item in another folder.This operation can also be used to delete files on BIM360 Document Management. For more information, please refer to the delete and restore a file tutorial.Before you use the Data Management API to access BIM 360 Docs files, you must provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param body: Describe the version to be created.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CreatedVersion]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.created_version400_error import CreatedVersion400Error
        from ......models.created_version403_error import CreatedVersion403Error
        from ......models.created_version404_error import CreatedVersion404Error
        from ......models.created_version423_error import CreatedVersion423Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": CreatedVersion400Error,
            "403": CreatedVersion403Error,
            "404": CreatedVersion404Error,
            "423": CreatedVersion423Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.created_version import CreatedVersion

        return await self.request_adapter.send_async(request_info, CreatedVersion, error_mapping)
    
    def to_post_request_information(self,body: VersionPayload, request_configuration: Optional[RequestConfiguration[VersionsRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates a new versions of an existing item.Before creating a new version you must create a storage location for the version in OSS, and upload the file to that location. For more details about the workflow, see the tutorial on uploading a file.This operation also allows you to create a new version of an item by copying a specific version of an existing item from another folder within the project. The new version becomes the tip version of the item.Use the [Create an Item](/en/docs/data/v2/reference/http/projects-project_id-items-POST/) operation to copy a specific version of an existing item as a new item in another folder.This operation can also be used to delete files on BIM360 Document Management. For more information, please refer to the delete and restore a file tutorial.Before you use the Data Management API to access BIM 360 Docs files, you must provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param body: Describe the version to be created.
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
    
    def with_url(self,raw_url: str) -> VersionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VersionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return VersionsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class VersionsRequestBuilderPostQueryParameters():
        """
        Creates a new versions of an existing item.Before creating a new version you must create a storage location for the version in OSS, and upload the file to that location. For more details about the workflow, see the tutorial on uploading a file.This operation also allows you to create a new version of an item by copying a specific version of an existing item from another folder within the project. The new version becomes the tip version of the item.Use the [Create an Item](/en/docs/data/v2/reference/http/projects-project_id-items-POST/) operation to copy a specific version of an existing item as a new item in another folder.This operation can also be used to delete files on BIM360 Document Management. For more information, please refer to the delete and restore a file tutorial.Before you use the Data Management API to access BIM 360 Docs files, you must provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "copy_from":
                return "copyFrom"
            return original_name
        
        # The Version ID (URN) of the version to copy from. **Note**: This parameter is relevant only for copying files to BIM 360 Docs.For information on how to find the URN, see the initial steps of the [Download a File](/en/docs/data/v2/tutorials/download-file/) tutorial.You can only copy files to the Plans folder or to subfolders of the Plans folder with an ``item:autodesk.bim360:Document`` item extension type. You can only copy files to the Project Files folder or to subfolders of the Project Files folder with an ``item:autodesk.bim360:File`` item extension type.  To verify an item’s extension type, use the [Get an Item](/en/docs/data/v2/reference/http/projects-project_id-items-item_id-GET/) operation, and check the ``attributes.extension.type`` attribute.  Note that if you copy a file to the Plans folder or to a subfolder of the Plans folder, the copied file inherits the permissions of the source file. For example, if users of your app did not have permission to download files in the source folder, but does have permission to download files in the target folder, they will not be able to download the copied file.  Note that you cannot copy a file while it is being uploaded, updated, or copied. To verify the current process state of a file, call the [Get an Item](en/docs/data/v2/reference/http/projects-project_id-items-item_id-GET/) operation , and check the ``attributes.extension.data.processState`` attribute.
        copy_from: Optional[str] = None

    
    @dataclass
    class VersionsRequestBuilderPostRequestConfiguration(RequestConfiguration[VersionsRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

