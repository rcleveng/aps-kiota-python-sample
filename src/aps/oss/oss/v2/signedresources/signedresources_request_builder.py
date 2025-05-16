from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_hash_item_request_builder import WithHashItemRequestBuilder

class SignedresourcesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/signedresources
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SignedresourcesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/signedresources", path_parameters)
    
    def by_hash(self,hash: str) -> WithHashItemRequestBuilder:
        """
        Gets an item from the ApiSdk.oss.v2.signedresources.item collection
        param hash: The ID component of the signed URL.**Note:** The signed URL returned by [Generate OSS Signed URL](/en/docs/data/v2/reference/http/signedresources-:id-GET/) contains ``hash`` as a URI parameter.
        Returns: WithHashItemRequestBuilder
        """
        if hash is None:
            raise TypeError("hash cannot be null.")
        from .item.with_hash_item_request_builder import WithHashItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["hash"] = hash
        return WithHashItemRequestBuilder(self.request_adapter, url_tpl_params)
    

