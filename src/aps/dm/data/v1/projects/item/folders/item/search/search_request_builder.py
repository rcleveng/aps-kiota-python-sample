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
    from ........models.search import Search
    from ........models.search400_error import Search400Error
    from ........models.search403_error import Search403Error
    from ........models.search404_error import Search404Error

class SearchRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/folders/{folder_id}/search
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SearchRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/folders/{folder_id}/search{?filter%5B%2A%5D*,page%5Bnumber%5D*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SearchRequestBuilderGetQueryParameters]] = None) -> Optional[Search]:
        """
        Searches the specified folder and its subfolders and returns a list of the latest versions of the items you can access.Use the ``filter`` query string parameter to narrow down the list as appropriate. You can filter by the following properties of the version payload: - ``type`` property, - ``id`` property, - any of the attributes object properties. For example, you can filter by ``createTime`` and ``mimeType``. It returns tip versions (latest versions) of properties where the filter conditions are satisfied. To verify the properties of the attributes object for a specific version, use the [Get a Version](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-GET/) operation.To list the immediate contents of the folder without parsing subfolders, use the [List Folder Contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET/) operation.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Search]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.search400_error import Search400Error
        from ........models.search403_error import Search403Error
        from ........models.search404_error import Search404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Search400Error,
            "403": Search403Error,
            "404": Search404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.search import Search

        return await self.request_adapter.send_async(request_info, Search, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SearchRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Searches the specified folder and its subfolders and returns a list of the latest versions of the items you can access.Use the ``filter`` query string parameter to narrow down the list as appropriate. You can filter by the following properties of the version payload: - ``type`` property, - ``id`` property, - any of the attributes object properties. For example, you can filter by ``createTime`` and ``mimeType``. It returns tip versions (latest versions) of properties where the filter conditions are satisfied. To verify the properties of the attributes object for a specific version, use the [Get a Version](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-GET/) operation.To list the immediate contents of the folder without parsing subfolders, use the [List Folder Contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET/) operation.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> SearchRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SearchRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SearchRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SearchRequestBuilderGetQueryParameters():
        """
        Searches the specified folder and its subfolders and returns a list of the latest versions of the items you can access.Use the ``filter`` query string parameter to narrow down the list as appropriate. You can filter by the following properties of the version payload: - ``type`` property, - ``id`` property, - any of the attributes object properties. For example, you can filter by ``createTime`` and ``mimeType``. It returns tip versions (latest versions) of properties where the filter conditions are satisfied. To verify the properties of the attributes object for a specific version, use the [Get a Version](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-GET/) operation.To list the immediate contents of the folder without parsing subfolders, use the [List Folder Contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET/) operation.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "filter":
                return "filter%5B%2A%5D"
            if original_name == "pagenumber":
                return "page%5Bnumber%5D"
            return original_name
        
        # Filter the data. See the [Filtering](/en/docs/data/v2/overview/filtering/) section for details.
        filter: Optional[list[str]] = None

        # Specifies what page to return. Page numbers are 0-based (the first page is page 0).
        pagenumber: Optional[int] = None

    
    @dataclass
    class SearchRequestBuilderGetRequestConfiguration(RequestConfiguration[SearchRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

