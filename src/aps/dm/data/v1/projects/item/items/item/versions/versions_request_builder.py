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
    from ........models.versions import Versions
    from ........models.versions400_error import Versions400Error
    from ........models.versions403_error import Versions403Error
    from ........models.versions404_error import Versions404Error

class VersionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/items/{item_id}/versions
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new VersionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/items/{item_id}/versions{?filter%5Bextension%2Etype%5D*,filter%5Bid%5D*,filter%5BversionNumber%5D*,page%5Blimit%5D*,page%5Bnumber%5D*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[VersionsRequestBuilderGetQueryParameters]] = None) -> Optional[Versions]:
        """
        Lists all versions of the specified item. A project can contain multiple versions of a resource item.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Versions]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.versions400_error import Versions400Error
        from ........models.versions403_error import Versions403Error
        from ........models.versions404_error import Versions404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Versions400Error,
            "403": Versions403Error,
            "404": Versions404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.versions import Versions

        return await self.request_adapter.send_async(request_info, Versions, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[VersionsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Lists all versions of the specified item. A project can contain multiple versions of a resource item.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> VersionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VersionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return VersionsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class VersionsRequestBuilderGetQueryParameters():
        """
        Lists all versions of the specified item. A project can contain multiple versions of a resource item.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "filterextension_type":
                return "filter%5Bextension%2Etype%5D"
            if original_name == "filterid":
                return "filter%5Bid%5D"
            if original_name == "filterversion_number":
                return "filter%5BversionNumber%5D"
            if original_name == "pagelimit":
                return "page%5Blimit%5D"
            if original_name == "pagenumber":
                return "page%5Bnumber%5D"
            return original_name
        
        # Filter by the extension type. 
        filterextension_type: Optional[list[str]] = None

        # Filter by the ``id`` of the ``ref`` target.
        filterid: Optional[list[str]] = None

        # Filter by versionNumber.
        filterversion_number: Optional[list[int]] = None

        # Specifies the maximum number of elements to return in the page. The default value is 200. The min value is 1. The max value is 200.
        pagelimit: Optional[int] = None

        # Specifies what page to return. Page numbers are 0-based (the first page is page 0).
        pagenumber: Optional[int] = None

    
    @dataclass
    class VersionsRequestBuilderGetRequestConfiguration(RequestConfiguration[VersionsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

