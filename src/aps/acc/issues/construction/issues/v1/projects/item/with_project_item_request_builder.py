from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .issues.issues_request_builder import IssuesRequestBuilder
    from .issue_attribute_definitions.issue_attribute_definitions_request_builder import IssueAttributeDefinitionsRequestBuilder
    from .issue_attribute_mappings.issue_attribute_mappings_request_builder import IssueAttributeMappingsRequestBuilder
    from .issue_root_cause_categories.issue_root_cause_categories_request_builder import IssueRootCauseCategoriesRequestBuilder
    from .issue_types.issue_types_request_builder import IssueTypesRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder

class WithProjectItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /construction/issues/v1/projects/{projectId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithProjectItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/construction/issues/v1/projects/{projectId}", path_parameters)
    
    @property
    def issues(self) -> IssuesRequestBuilder:
        """
        The issues property
        """
        from .issues.issues_request_builder import IssuesRequestBuilder

        return IssuesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def issue_attribute_definitions(self) -> IssueAttributeDefinitionsRequestBuilder:
        """
        The issueAttributeDefinitions property
        """
        from .issue_attribute_definitions.issue_attribute_definitions_request_builder import IssueAttributeDefinitionsRequestBuilder

        return IssueAttributeDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def issue_attribute_mappings(self) -> IssueAttributeMappingsRequestBuilder:
        """
        The issueAttributeMappings property
        """
        from .issue_attribute_mappings.issue_attribute_mappings_request_builder import IssueAttributeMappingsRequestBuilder

        return IssueAttributeMappingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def issue_root_cause_categories(self) -> IssueRootCauseCategoriesRequestBuilder:
        """
        The issueRootCauseCategories property
        """
        from .issue_root_cause_categories.issue_root_cause_categories_request_builder import IssueRootCauseCategoriesRequestBuilder

        return IssueRootCauseCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def issue_types(self) -> IssueTypesRequestBuilder:
        """
        The issueTypes property
        """
        from .issue_types.issue_types_request_builder import IssueTypesRequestBuilder

        return IssueTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        The users property
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    

