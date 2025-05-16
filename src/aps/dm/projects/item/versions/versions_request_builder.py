from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_version_item_request_builder import WithVersion_ItemRequestBuilder

class VersionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{project_id}/versions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VersionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{project_id}/versions", path_parameters)
    
    def by_version_id(self,version_id: str) -> WithVersion_ItemRequestBuilder:
        """
        Gets an item from the ApiSdk.projects.item.versions.item collection
        param version_id: The URL encoded unique identifier of a version.
        Returns: WithVersion_ItemRequestBuilder
        """
        if version_id is None:
            raise TypeError("version_id cannot be null.")
        from .item.with_version_item_request_builder import WithVersion_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["version_id"] = version_id
        return WithVersion_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

