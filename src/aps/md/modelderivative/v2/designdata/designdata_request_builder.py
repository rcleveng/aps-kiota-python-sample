from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .formats.formats_request_builder import FormatsRequestBuilder
    from .item.with_urn_item_request_builder import WithUrnItemRequestBuilder
    from .job.job_request_builder import JobRequestBuilder

class DesigndataRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DesigndataRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata", path_parameters)
    
    def by_urn(self,urn: str) -> WithUrnItemRequestBuilder:
        """
        Gets an item from the ApiSdk.modelderivative.v2.designdata.item collection
        param urn: The URL-safe Base64 encoded URN of the source design.
        Returns: WithUrnItemRequestBuilder
        """
        if urn is None:
            raise TypeError("urn cannot be null.")
        from .item.with_urn_item_request_builder import WithUrnItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["urn"] = urn
        return WithUrnItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def formats(self) -> FormatsRequestBuilder:
        """
        The formats property
        """
        from .formats.formats_request_builder import FormatsRequestBuilder

        return FormatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def job(self) -> JobRequestBuilder:
        """
        The job property
        """
        from .job.job_request_builder import JobRequestBuilder

        return JobRequestBuilder(self.request_adapter, self.path_parameters)
    

