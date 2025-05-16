from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .commands.commands_request_builder import CommandsRequestBuilder
    from .downloads.downloads_request_builder import DownloadsRequestBuilder
    from .folders.folders_request_builder import FoldersRequestBuilder
    from .items.items_request_builder import ItemsRequestBuilder
    from .jobs.jobs_request_builder import JobsRequestBuilder
    from .storage.storage_request_builder import StorageRequestBuilder
    from .versions.versions_request_builder import VersionsRequestBuilder

class WithProject_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithProject_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}", path_parameters)
    
    @property
    def commands(self) -> CommandsRequestBuilder:
        """
        The commands property
        """
        from .commands.commands_request_builder import CommandsRequestBuilder

        return CommandsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def downloads(self) -> DownloadsRequestBuilder:
        """
        The downloads property
        """
        from .downloads.downloads_request_builder import DownloadsRequestBuilder

        return DownloadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def folders(self) -> FoldersRequestBuilder:
        """
        The folders property
        """
        from .folders.folders_request_builder import FoldersRequestBuilder

        return FoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> ItemsRequestBuilder:
        """
        The items property
        """
        from .items.items_request_builder import ItemsRequestBuilder

        return ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> JobsRequestBuilder:
        """
        The jobs property
        """
        from .jobs.jobs_request_builder import JobsRequestBuilder

        return JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storage(self) -> StorageRequestBuilder:
        """
        The storage property
        """
        from .storage.storage_request_builder import StorageRequestBuilder

        return StorageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> VersionsRequestBuilder:
        """
        The versions property
        """
        from .versions.versions_request_builder import VersionsRequestBuilder

        return VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    

