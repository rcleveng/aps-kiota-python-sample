from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .buckets.buckets_request_builder import BucketsRequestBuilder
    from .signedresources.signedresources_request_builder import SignedresourcesRequestBuilder

class V2RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V2RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2", path_parameters)
    
    @property
    def buckets(self) -> BucketsRequestBuilder:
        """
        The buckets property
        """
        from .buckets.buckets_request_builder import BucketsRequestBuilder

        return BucketsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def signedresources(self) -> SignedresourcesRequestBuilder:
        """
        The signedresources property
        """
        from .signedresources.signedresources_request_builder import SignedresourcesRequestBuilder

        return SignedresourcesRequestBuilder(self.request_adapter, self.path_parameters)
    

