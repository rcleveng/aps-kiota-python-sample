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
    from ........models.issue import Issue
    from ........models.issue_payload import IssuePayload
    from .comments.comments_request_builder import CommentsRequestBuilder

class WithIssueItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /construction/issues/v1/projects/{projectId}/issues/{issueId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithIssueItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/construction/issues/v1/projects/{projectId}/issues/{issueId}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Issue]:
        """
        Retrieves detailed information about a single issue. For general information about all the issues in a project.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Issue]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.issue import Issue

        return await self.request_adapter.send_async(request_info, Issue, None)
    
    async def patch(self,body: IssuePayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Issue]:
        """
        Updates an issue.To verify whether a user can update issues for a specific project, call GET users/me.To verify which attributes the user can update, call GET issues/:id and check the permittedAttributes and permittedStatuses lists.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Issue]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.issue import Issue

        return await self.request_adapter.send_async(request_info, Issue, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Retrieves detailed information about a single issue. For general information about all the issues in a project.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: IssuePayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates an issue.To verify whether a user can update issues for a specific project, call GET users/me.To verify which attributes the user can update, call GET issues/:id and check the permittedAttributes and permittedStatuses lists.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WithIssueItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithIssueItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithIssueItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def comments(self) -> CommentsRequestBuilder:
        """
        The comments property
        """
        from .comments.comments_request_builder import CommentsRequestBuilder

        return CommentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithIssueItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithIssueItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

