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
    from ........models.properties import Properties

class PropertiesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PropertiesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties{?forceget*,objectid*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderGetQueryParameters]] = None) -> Optional[Properties]:
        """
        Returns a list of properties of all objects in the  Model View specified by the ``modelGuid`` parameter. This operation returns properties of all objects by default. However, you can restrict the results to a specific object by specifying its ID as the ``objectid`` parameter.Properties are returned as a flat list, ordered, by their ``objectid``. The ``objectid`` is a non-persistent ID assigned to an object when the source design is translated to the SVF or SVF2 format. This means that:- A design file must be translated to SVF or SVF2 before you can retrieve properties.- The ``objectid`` of an object can change if the design is translated to SVF or SVF2 again. If you require a persistent ID across translations, use ``externalId`` to reference objects, instead of ``objectid``.Before you call this operation:- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views (Viewables) in the source design. - Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid`` parameter.**Tip**: Use `Fetch Specific Properties </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-guid-properties-query-POST/>`_ to retrieve only the objects and properties of interest. What’s more, the response is paginated. So, when the number of properties returned is large, responses start arriving more promptly.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Properties]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.properties import Properties

        return await self.request_adapter.send_async(request_info, Properties, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PropertiesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of properties of all objects in the  Model View specified by the ``modelGuid`` parameter. This operation returns properties of all objects by default. However, you can restrict the results to a specific object by specifying its ID as the ``objectid`` parameter.Properties are returned as a flat list, ordered, by their ``objectid``. The ``objectid`` is a non-persistent ID assigned to an object when the source design is translated to the SVF or SVF2 format. This means that:- A design file must be translated to SVF or SVF2 before you can retrieve properties.- The ``objectid`` of an object can change if the design is translated to SVF or SVF2 again. If you require a persistent ID across translations, use ``externalId`` to reference objects, instead of ``objectid``.Before you call this operation:- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views (Viewables) in the source design. - Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid`` parameter.**Tip**: Use `Fetch Specific Properties </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-guid-properties-query-POST/>`_ to retrieve only the objects and properties of interest. What’s more, the response is paginated. So, when the number of properties returned is large, responses start arriving more promptly.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PropertiesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PropertiesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PropertiesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PropertiesRequestBuilderGetQueryParameters():
        """
        Returns a list of properties of all objects in the  Model View specified by the ``modelGuid`` parameter. This operation returns properties of all objects by default. However, you can restrict the results to a specific object by specifying its ID as the ``objectid`` parameter.Properties are returned as a flat list, ordered, by their ``objectid``. The ``objectid`` is a non-persistent ID assigned to an object when the source design is translated to the SVF or SVF2 format. This means that:- A design file must be translated to SVF or SVF2 before you can retrieve properties.- The ``objectid`` of an object can change if the design is translated to SVF or SVF2 again. If you require a persistent ID across translations, use ``externalId`` to reference objects, instead of ``objectid``.Before you call this operation:- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views (Viewables) in the source design. - Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid`` parameter.**Tip**: Use `Fetch Specific Properties </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-guid-properties-query-POST/>`_ to retrieve only the objects and properties of interest. What’s more, the response is paginated. So, when the number of properties returned is large, responses start arriving more promptly.
        """
        # ``true``: Retrieves large resources, even beyond the 20 MB limit. If exceptionally large (over 800 MB), the system acts as if ``forceget`` is ``false``. ``false``: (Default) Does not retrieve resources if they are larger than 20 MB.
        forceget: Optional[str] = None

        # The Object ID of the object you want to restrict the response to. If you do not specify this parameter, all properties of all objects within the Model View are returned.  
        objectid: Optional[int] = None

    
    @dataclass
    class PropertiesRequestBuilderGetRequestConfiguration(RequestConfiguration[PropertiesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

