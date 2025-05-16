from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_new_obj_key_item_request_builder import WithNewObjKeyItemRequestBuilder

class CopytoRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/buckets/{bucketKey}/objects/{objectKey}/copyto
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CopytoRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/buckets/{bucketKey}/objects/{objectKey}/copyto", path_parameters)
    
    def by_new_obj_key(self,new_obj_key: str) -> WithNewObjKeyItemRequestBuilder:
        """
        Gets an item from the ApiSdk.oss.v2.buckets.item.objects.item.copyto.item collection
        param new_obj_key: A URL-encoded human friendly name to identify the copied object.
        Returns: WithNewObjKeyItemRequestBuilder
        """
        if new_obj_key is None:
            raise TypeError("new_obj_key cannot be null.")
        from .item.with_new_obj_key_item_request_builder import WithNewObjKeyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["newObjKey"] = new_obj_key
        return WithNewObjKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    

