from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .manifest.manifest_request_builder import ManifestRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .references.references_request_builder import ReferencesRequestBuilder
    from .thumbnail.thumbnail_request_builder import ThumbnailRequestBuilder

class WithUrnItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata/{urn}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithUrnItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata/{urn}", path_parameters)
    
    @property
    def manifest(self) -> ManifestRequestBuilder:
        """
        The manifest property
        """
        from .manifest.manifest_request_builder import ManifestRequestBuilder

        return ManifestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def references(self) -> ReferencesRequestBuilder:
        """
        The references property
        """
        from .references.references_request_builder import ReferencesRequestBuilder

        return ReferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thumbnail(self) -> ThumbnailRequestBuilder:
        """
        The thumbnail property
        """
        from .thumbnail.thumbnail_request_builder import ThumbnailRequestBuilder

        return ThumbnailRequestBuilder(self.request_adapter, self.path_parameters)
    

