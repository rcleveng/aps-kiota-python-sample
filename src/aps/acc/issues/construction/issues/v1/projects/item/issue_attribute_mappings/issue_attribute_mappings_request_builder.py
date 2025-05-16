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
    from .......models.attr_mapping_page import Attr_mapping_page

class IssueAttributeMappingsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /construction/issues/v1/projects/{projectId}/issue-attribute-mappings
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IssueAttributeMappingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/construction/issues/v1/projects/{projectId}/issue-attribute-mappings{?filter%5BattributeDefinitionId%5D*,filter%5BcreatedAt%5D*,filter%5BdeletedAt%5D*,filter%5BmappedItemId%5D*,filter%5BupdatedAt%5D*,limit*,offset*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IssueAttributeMappingsRequestBuilderGetQueryParameters]] = None) -> Optional[Attr_mapping_page]:
        """
        Retrieves information about the issue custom attributes (custom fields) that are assigned to issue categories and issue types.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Attr_mapping_page]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.attr_mapping_page import Attr_mapping_page

        return await self.request_adapter.send_async(request_info, Attr_mapping_page, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IssueAttributeMappingsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieves information about the issue custom attributes (custom fields) that are assigned to issue categories and issue types.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> IssueAttributeMappingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IssueAttributeMappingsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IssueAttributeMappingsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class IssueAttributeMappingsRequestBuilderGetQueryParameters():
        """
        Retrieves information about the issue custom attributes (custom fields) that are assigned to issue categories and issue types.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "filterattribute_definition_id":
                return "filter%5BattributeDefinitionId%5D"
            if original_name == "filtercreated_at":
                return "filter%5BcreatedAt%5D"
            if original_name == "filterdeleted_at":
                return "filter%5BdeletedAt%5D"
            if original_name == "filtermapped_item_id":
                return "filter%5BmappedItemId%5D"
            if original_name == "filterupdated_at":
                return "filter%5BupdatedAt%5D"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            return original_name
        
        # Retrieves issue custom attribute mappings associated with the specified issue custom attribute definitions. Separate multiple values with commas. For example: filter[attributeDefinitionId]=18ee5858-cbf1-451a-a525-7c6ff8156775.
        filterattribute_definition_id: Optional[str] = None

        # Retrieves items that were created at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
        filtercreated_at: Optional[str] = None

        # Retrieves types that were deleted at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
        filterdeleted_at: Optional[str] = None

        # Retrieves issue custom attribute mappings associated with the specified items (project, type, or subtype). Separate multiple values with commas. For example: filter[mappedItemId]=18ee5858-cbf1-451a-a525-7c6ff8156775. Note that this does not retrieve inherited custom attribute mappings or custom attribute mappings of descendants.
        filtermapped_item_id: Optional[str] = None

        # Retrieves items that were last updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
        filterupdated_at: Optional[str] = None

        # The number of custom attribute mappings to return in the response payload. For example, limit=2. Acceptable values: 1-200. Default value: 200.
        limit: Optional[int] = None

        # The number of custom attribute mappings you want to begin retrieving results from.
        offset: Optional[int] = None

    
    @dataclass
    class IssueAttributeMappingsRequestBuilderGetRequestConfiguration(RequestConfiguration[IssueAttributeMappingsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

