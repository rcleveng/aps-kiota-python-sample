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
    from ........models.specific_properties import SpecificProperties
    from ........models.specific_properties_payload import SpecificPropertiesPayload

class PropertiesQueryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties:query
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PropertiesQueryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties:query", path_parameters)
    
    async def post(self,body: SpecificPropertiesPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SpecificProperties]:
        """
        Queries the objects in the Model View (Viewable) specified by the ``modelGuid`` parameter and returns the specified properties in a paginated list. You can limit the number of objects to be queried by specifying a filter using the ``query`` attribute in the request body.**Note:** A design file must be translated to SVF or SVF2 before you can query object properties.  Before you call this operation:- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views in the source design.- Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid``  parameter.
        param body: An object that represents the request body of a Fetch Specific Properties operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SpecificProperties]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.specific_properties import SpecificProperties

        return await self.request_adapter.send_async(request_info, SpecificProperties, None)
    
    def to_post_request_information(self,body: SpecificPropertiesPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Queries the objects in the Model View (Viewable) specified by the ``modelGuid`` parameter and returns the specified properties in a paginated list. You can limit the number of objects to be queried by specifying a filter using the ``query`` attribute in the request body.**Note:** A design file must be translated to SVF or SVF2 before you can query object properties.  Before you call this operation:- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views in the source design.- Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid``  parameter.
        param body: An object that represents the request body of a Fetch Specific Properties operation.
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
    
    def with_url(self,raw_url: str) -> PropertiesQueryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PropertiesQueryRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PropertiesQueryRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PropertiesQueryRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

