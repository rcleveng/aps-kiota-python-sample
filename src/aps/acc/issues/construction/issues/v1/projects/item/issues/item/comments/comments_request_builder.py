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
    from .........models.comments import Comments
    from .........models.comments_payload import CommentsPayload
    from .........models.sort_by import SortBy

class CommentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /construction/issues/v1/projects/{projectId}/issues/{issueId}/comments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CommentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/construction/issues/v1/projects/{projectId}/issues/{issueId}/comments{?limit*,offset*,sortBy*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CommentsRequestBuilderGetQueryParameters]] = None) -> Optional[Comments]:
        """
        Get all the comments for a specific issue.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Comments]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.comments import Comments

        return await self.request_adapter.send_async(request_info, Comments, None)
    
    async def post(self,body: CommentsPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Comments]:
        """
        Creates a new comment under a specific issue.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Comments]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.comments import Comments

        return await self.request_adapter.send_async(request_info, Comments, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CommentsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get all the comments for a specific issue.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CommentsPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new comment under a specific issue.
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> CommentsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CommentsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CommentsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CommentsRequestBuilderGetQueryParameters():
        """
        Get all the comments for a specific issue.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "sort_by":
                return "sortBy"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            return original_name
        
        # Add limit=20 to limit the results count (together with the offset to support pagination).
        limit: Optional[str] = None

        # Add offset=20 to get partial results (together with the limit to support pagination).
        offset: Optional[str] = None

        # Sort issue comments by specified fields. Separate multiple values with commas. To sort in descending order add a - (minus sign) before the sort criteria
        sort_by: list[SortBy] = field(default_factory=list)

    
    @dataclass
    class CommentsRequestBuilderGetRequestConfiguration(RequestConfiguration[CommentsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CommentsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

