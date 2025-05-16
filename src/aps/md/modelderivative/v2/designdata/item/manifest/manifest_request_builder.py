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
    from ......models.delete_manifest import DeleteManifest
    from ......models.manifest import Manifest
    from .item.with_derivative_urn_item_request_builder import WithDerivativeUrnItemRequestBuilder

class ManifestRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata/{urn}/manifest
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ManifestRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata/{urn}/manifest", path_parameters)
    
    def by_derivative_urn(self,derivative_urn: str) -> WithDerivativeUrnItemRequestBuilder:
        """
        Gets an item from the ApiSdk.modelderivative.v2.designdata.item.manifest.item collection
        param derivative_urn: The URL-encoded URN of the derivative. Check the manifest of the source design to get the URNs of the derivatives available for download.
        Returns: WithDerivativeUrnItemRequestBuilder
        """
        if derivative_urn is None:
            raise TypeError("derivative_urn cannot be null.")
        from .item.with_derivative_urn_item_request_builder import WithDerivativeUrnItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["derivativeUrn"] = derivative_urn
        return WithDerivativeUrnItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeleteManifest]:
        """
        Deletes the manifest of the specified source design. It also deletes all derivatives (translated output files) generated from the source design. However, it does not delete the source design.**Note:** This operation is idempotent. So, if you call it multiple times, even when no manifest exists, will still return a successful response (200).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeleteManifest]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.delete_manifest import DeleteManifest

        return await self.request_adapter.send_async(request_info, DeleteManifest, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Manifest]:
        """
        Retrieves the manifest of the specified source design.The manifest is a JSON file containing information about all the derivatives translated from the specified source design. It contains information such as the URNs of the derivatives, the translation status of each derivative, and much more.The first time you translate a source design, the Model Derivative service creates a manifest for that design. Thereafter, every time you translate that source design, even to a different format, the Model Derivative service updates the same manifest. It does not create a new manifest. Instead, the manifest acts like a central registry for all the derivatives of your source design created through the Model Derivative service.  When the Model Derivative service starts a translation job (as a result of a request you make using `Create Translation Job </en/docs/model-derivative/v2/reference/http/jobs/job-POST/>`_), it keeps on updating the manifest at regular intervals. So, you can use the manifest to check the status and progress of each derivative that is being generated. When multiple derivatives have been requested each derivative may complete at a different time. So, each derivative has its own ``status`` attribute. The manifest also contains an overall ``status`` attribute. The overall ``status`` becomes ``complete`` when the ``status`` of all individual derivatives become complete.Once the translation status of a derivative is ``complete`` you can download the derivative.**Note:** You cannot download 3D SVF2 derivatives.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Manifest]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.manifest import Manifest

        return await self.request_adapter.send_async(request_info, Manifest, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes the manifest of the specified source design. It also deletes all derivatives (translated output files) generated from the source design. However, it does not delete the source design.**Note:** This operation is idempotent. So, if you call it multiple times, even when no manifest exists, will still return a successful response (200).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Retrieves the manifest of the specified source design.The manifest is a JSON file containing information about all the derivatives translated from the specified source design. It contains information such as the URNs of the derivatives, the translation status of each derivative, and much more.The first time you translate a source design, the Model Derivative service creates a manifest for that design. Thereafter, every time you translate that source design, even to a different format, the Model Derivative service updates the same manifest. It does not create a new manifest. Instead, the manifest acts like a central registry for all the derivatives of your source design created through the Model Derivative service.  When the Model Derivative service starts a translation job (as a result of a request you make using `Create Translation Job </en/docs/model-derivative/v2/reference/http/jobs/job-POST/>`_), it keeps on updating the manifest at regular intervals. So, you can use the manifest to check the status and progress of each derivative that is being generated. When multiple derivatives have been requested each derivative may complete at a different time. So, each derivative has its own ``status`` attribute. The manifest also contains an overall ``status`` attribute. The overall ``status`` becomes ``complete`` when the ``status`` of all individual derivatives become complete.Once the translation status of a derivative is ``complete`` you can download the derivative.**Note:** You cannot download 3D SVF2 derivatives.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ManifestRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManifestRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ManifestRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ManifestRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManifestRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

