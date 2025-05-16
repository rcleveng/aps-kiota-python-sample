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
    from ......models.model_views import ModelViews
    from .item.with_model_gu_item_request_builder import WithModelGuItemRequestBuilder

class MetadataRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata/{urn}/metadata
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MetadataRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata/{urn}/metadata", path_parameters)
    
    def by_model_guid(self,model_guid: str) -> WithModelGuItemRequestBuilder:
        """
        Gets an item from the ApiSdk.modelderivative.v2.designdata.item.metadata.item collection
        param model_guid: The ID of the Model View you are extracting the object tree from. Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET>`_ operation to get the IDs of the Model Views in the source design.
        Returns: WithModelGuItemRequestBuilder
        """
        if model_guid is None:
            raise TypeError("model_guid cannot be null.")
        from .item.with_model_gu_item_request_builder import WithModelGuItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["modelGuid"] = model_guid
        return WithModelGuItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ModelViews]:
        """
        Returns a list of Model Views (Viewables) in the source design specified by the ``urn`` parameter. It also returns an ID that uniquely identifies the Model View. You can use these IDs with other metadata operations to obtain information about the objects within those Model Views.Designs created with applications like Fusion 360 and Inventor contain only one Model View per design. Applications like Revit allow multiple Model Views per design.**Note:** You can retrieve metadata only from a design that has already been translated to SVF or SVF2.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ModelViews]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.model_views import ModelViews

        return await self.request_adapter.send_async(request_info, ModelViews, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of Model Views (Viewables) in the source design specified by the ``urn`` parameter. It also returns an ID that uniquely identifies the Model View. You can use these IDs with other metadata operations to obtain information about the objects within those Model Views.Designs created with applications like Fusion 360 and Inventor contain only one Model View per design. Applications like Revit allow multiple Model Views per design.**Note:** You can retrieve metadata only from a design that has already been translated to SVF or SVF2.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MetadataRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MetadataRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MetadataRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MetadataRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

