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
    from ......models.specify_references import SpecifyReferences
    from ......models.specify_references_payload import SpecifyReferencesPayload

class ReferencesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata/{urn}/references
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ReferencesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata/{urn}/references", path_parameters)
    
    async def post(self,body: SpecifyReferencesPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SpecifyReferences]:
        """
        Specifies the location of the files referenced by the specified source design.When you call `Create Translation Job </en/docs/model-derivative/v2/reference/http/job-POST>`_, set  ``checkReferences`` to ``true``.   The Model Derivative service will then use the details you specify in this operation to locate and download the referenced files.
        param body: An object that represents the successful response of a Specify References operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SpecifyReferences]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.specify_references import SpecifyReferences

        return await self.request_adapter.send_async(request_info, SpecifyReferences, None)
    
    def to_post_request_information(self,body: SpecifyReferencesPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Specifies the location of the files referenced by the specified source design.When you call `Create Translation Job </en/docs/model-derivative/v2/reference/http/job-POST>`_, set  ``checkReferences`` to ``true``.   The Model Derivative service will then use the details you specify in this operation to locate and download the referenced files.
        param body: An object that represents the successful response of a Specify References operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ReferencesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ReferencesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ReferencesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ReferencesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

