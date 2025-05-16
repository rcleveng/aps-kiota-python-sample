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
    from .......models.modify_version_payload import ModifyVersionPayload
    from .......models.version import Version
    from .......models.version400_error import Version400Error
    from .......models.version403_error import Version403Error
    from .......models.version404_error import Version404Error
    from .......models.version423_error import Version423Error
    from .downloads.downloads_request_builder import DownloadsRequestBuilder
    from .download_formats.download_formats_request_builder import DownloadFormatsRequestBuilder
    from .item_escaped.item_escaped_request_builder import Item_EscapedRequestBuilder
    from .refs.refs_request_builder import RefsRequestBuilder
    from .relationships.relationships_request_builder import RelationshipsRequestBuilder

class WithVersion_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/versions/{version_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithVersion_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/versions/{version_id}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Version]:
        """
        Returns the specified version of an item.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Version]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.version400_error import Version400Error
        from .......models.version403_error import Version403Error
        from .......models.version404_error import Version404Error
        from .......models.version423_error import Version423Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Version400Error,
            "403": Version403Error,
            "404": Version404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.version import Version

        return await self.request_adapter.send_async(request_info, Version, error_mapping)
    
    async def patch(self,body: ModifyVersionPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Version]:
        """
        Updates the properties of the specified version of an  item. Currently, you can only change the name of the version.**Note:** This operation is not supported for BIM 360 and ACC. If you want to rename a version, create a new version with a new name.
        param body: An object that contains the information on the version to be patched.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Version]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.version400_error import Version400Error
        from .......models.version403_error import Version403Error
        from .......models.version404_error import Version404Error
        from .......models.version423_error import Version423Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Version400Error,
            "403": Version403Error,
            "404": Version404Error,
            "423": Version423Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.version import Version

        return await self.request_adapter.send_async(request_info, Version, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the specified version of an item.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ModifyVersionPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the properties of the specified version of an  item. Currently, you can only change the name of the version.**Note:** This operation is not supported for BIM 360 and ACC. If you want to rename a version, create a new version with a new name.
        param body: An object that contains the information on the version to be patched.
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
    
    def with_url(self,raw_url: str) -> WithVersion_ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithVersion_ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithVersion_ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def downloads(self) -> DownloadsRequestBuilder:
        """
        The downloads property
        """
        from .downloads.downloads_request_builder import DownloadsRequestBuilder

        return DownloadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def download_formats(self) -> DownloadFormatsRequestBuilder:
        """
        The downloadFormats property
        """
        from .download_formats.download_formats_request_builder import DownloadFormatsRequestBuilder

        return DownloadFormatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item(self) -> Item_EscapedRequestBuilder:
        """
        The item property
        """
        from .item_escaped.item_escaped_request_builder import Item_EscapedRequestBuilder

        return Item_EscapedRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    @dataclass
    class WithVersion_ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithVersion_ItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

