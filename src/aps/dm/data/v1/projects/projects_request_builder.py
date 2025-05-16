from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_project_item_request_builder import WithProject_ItemRequestBuilder

class ProjectsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ProjectsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects", path_parameters)
    
    def by_project_id(self,project_id: str) -> WithProject_ItemRequestBuilder:
        """
        Gets an item from the ApiSdk.data.v1.projects.item collection
        param project_id: The unique identifier of a project. For BIM 360 Docs and ACC Docs, a hub ID corresponds to an Account ID. To convert a BIM 360 or ACC Account ID to a hub ID, prefix the Account ID with ``b.``. For example, an Account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.Similarly, to convert an ACC or BIM 360 project ID to a Data Management project ID prefix the ACC or BIM 360 project ID with ``b.``. For example, a project ID of ``c8b0c73d-3ae9`` translates to a project ID of ``b.c8b0c73d-3ae9``.
        Returns: WithProject_ItemRequestBuilder
        """
        if project_id is None:
            raise TypeError("project_id cannot be null.")
        from .item.with_project_item_request_builder import WithProject_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["project_id"] = project_id
        return WithProject_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

