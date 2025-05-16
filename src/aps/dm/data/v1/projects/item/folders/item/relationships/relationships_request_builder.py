from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .links.links_request_builder import LinksRequestBuilder
    from .refs.refs_request_builder import RefsRequestBuilder

class RelationshipsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/folders/{folder_id}/relationships
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RelationshipsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/folders/{folder_id}/relationships", path_parameters)
    
    @property
    def links(self) -> LinksRequestBuilder:
        """
        The links property
        """
        from .links.links_request_builder import LinksRequestBuilder

        return LinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def refs(self) -> RefsRequestBuilder:
        """
        The refs property
        """
        from .refs.refs_request_builder import RefsRequestBuilder

        return RefsRequestBuilder(self.request_adapter, self.path_parameters)
    

