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
    from .......models.root_cause_categories_page import Root_cause_categories_page

class IssueRootCauseCategoriesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /construction/issues/v1/projects/{projectId}/issue-root-cause-categories
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IssueRootCauseCategoriesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/construction/issues/v1/projects/{projectId}/issue-root-cause-categories{?filter%5BupdatedAt%5D*,include*,limit*,offset*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IssueRootCauseCategoriesRequestBuilderGetQueryParameters]] = None) -> Optional[Root_cause_categories_page]:
        """
        Retrieves a list of supported root cause categories and root causes that you can allocate to an issue. For example, communication and coordination.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Root_cause_categories_page]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.root_cause_categories_page import Root_cause_categories_page

        return await self.request_adapter.send_async(request_info, Root_cause_categories_page, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IssueRootCauseCategoriesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieves a list of supported root cause categories and root causes that you can allocate to an issue. For example, communication and coordination.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> IssueRootCauseCategoriesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IssueRootCauseCategoriesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IssueRootCauseCategoriesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class IssueRootCauseCategoriesRequestBuilderGetQueryParameters():
        """
        Retrieves a list of supported root cause categories and root causes that you can allocate to an issue. For example, communication and coordination.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "filterupdated_at":
                return "filter%5BupdatedAt%5D"
            if original_name == "include":
                return "include"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            return original_name
        
        # Retrieves root cause categories updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
        filterupdated_at: Optional[str] = None

        # Add ‘include=rootcauses’ to add the root causes for each category.
        include: Optional[str] = None

        # Add limit=20 to limit the results count (together with the offset to support pagination).
        limit: Optional[int] = None

        # Add offset=20 to get partial results (together with the limit to support pagination)
        offset: Optional[int] = None

    
    @dataclass
    class IssueRootCauseCategoriesRequestBuilderGetRequestConfiguration(RequestConfiguration[IssueRootCauseCategoriesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

