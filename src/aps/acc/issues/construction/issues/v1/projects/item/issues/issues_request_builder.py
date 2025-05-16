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
    from .......models.fields import Fields
    from .......models.issue import Issue
    from .......models.issues_page import IssuesPage
    from .......models.issue_payload import IssuePayload
    from .......models.sort_by import SortBy
    from .item.with_issue_item_request_builder import WithIssueItemRequestBuilder

class IssuesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /construction/issues/v1/projects/{projectId}/issues
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IssuesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/construction/issues/v1/projects/{projectId}/issues{?fields*,filter%5BassignedToType%5D*,filter%5BassignedTo%5D*,filter%5BclosedAt%5D*,filter%5BclosedBy%5D*,filter%5BcreatedAt%5D*,filter%5BcreatedBy%5D*,filter%5BcustomAttributes%5D*,filter%5Bdeleted%5D*,filter%5BdisplayId%5D*,filter%5BdueDate%5D*,filter%5Bid%5D*,filter%5BissueSubtypeId%5D*,filter%5BissueTypeId%5D*,filter%5BlinkedDocumentUrn%5D*,filter%5BlocationId%5D*,filter%5BrootCauseId%5D*,filter%5Bsearch%5D*,filter%5BstartDate%5D*,filter%5Bstatus%5D*,filter%5BsubLocationId%5D*,filter%5BupdatedAt%5D*,filter%5BupdatedBy%5D*,filter%5Bvalid%5D*,limit*,offset*,sortBy*}", path_parameters)
    
    def by_issue_id(self,issue_id: str) -> WithIssueItemRequestBuilder:
        """
        Gets an item from the ApiSdk.construction.issues.v1.projects.item.issues.item collection
        param issue_id: The unique identifier of the issue.
        Returns: WithIssueItemRequestBuilder
        """
        if issue_id is None:
            raise TypeError("issue_id cannot be null.")
        from .item.with_issue_item_request_builder import WithIssueItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["issueId"] = issue_id
        return WithIssueItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IssuesRequestBuilderGetQueryParameters]] = None) -> Optional[IssuesPage]:
        """
        Retrieves information about all the issues in a project, including details about their associated comments and attachments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IssuesPage]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.issues_page import IssuesPage

        return await self.request_adapter.send_async(request_info, IssuesPage, None)
    
    async def post(self,body: IssuePayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Issue]:
        """
        Adds an issue to a project.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Issue]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.issue import Issue

        return await self.request_adapter.send_async(request_info, Issue, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IssuesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieves information about all the issues in a project, including details about their associated comments and attachments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: IssuePayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds an issue to a project.
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
    
    def with_url(self,raw_url: str) -> IssuesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IssuesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IssuesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class IssuesRequestBuilderGetQueryParameters():
        """
        Retrieves information about all the issues in a project, including details about their associated comments and attachments.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "filterassigned_to":
                return "filter%5BassignedTo%5D"
            if original_name == "filterassigned_to_type":
                return "filter%5BassignedToType%5D"
            if original_name == "filterclosed_at":
                return "filter%5BclosedAt%5D"
            if original_name == "filterclosed_by":
                return "filter%5BclosedBy%5D"
            if original_name == "filtercreated_at":
                return "filter%5BcreatedAt%5D"
            if original_name == "filtercreated_by":
                return "filter%5BcreatedBy%5D"
            if original_name == "filtercustom_attributes":
                return "filter%5BcustomAttributes%5D"
            if original_name == "filterdeleted":
                return "filter%5Bdeleted%5D"
            if original_name == "filterdisplay_id":
                return "filter%5BdisplayId%5D"
            if original_name == "filterdue_date":
                return "filter%5BdueDate%5D"
            if original_name == "filterid":
                return "filter%5Bid%5D"
            if original_name == "filterissue_subtype_id":
                return "filter%5BissueSubtypeId%5D"
            if original_name == "filterissue_type_id":
                return "filter%5BissueTypeId%5D"
            if original_name == "filterlinked_document_urn":
                return "filter%5BlinkedDocumentUrn%5D"
            if original_name == "filterlocation_id":
                return "filter%5BlocationId%5D"
            if original_name == "filterroot_cause_id":
                return "filter%5BrootCauseId%5D"
            if original_name == "filtersearch":
                return "filter%5Bsearch%5D"
            if original_name == "filterstart_date":
                return "filter%5BstartDate%5D"
            if original_name == "filterstatus":
                return "filter%5Bstatus%5D"
            if original_name == "filtersub_location_id":
                return "filter%5BsubLocationId%5D"
            if original_name == "filterupdated_at":
                return "filter%5BupdatedAt%5D"
            if original_name == "filterupdated_by":
                return "filter%5BupdatedBy%5D"
            if original_name == "filtervalid":
                return "filter%5Bvalid%5D"
            if original_name == "sort_by":
                return "sortBy"
            if original_name == "fields":
                return "fields"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            return original_name
        
        # Return only specific fields in issue object. Separate multiple values with commas.
        fields: list[Fields] = field(default_factory=list)

        # Filter issues by the unique Autodesk ID of the User/Company/Role identifier of the current assignee of this issue. Separate multiple values with commas.
        filterassigned_to: Optional[list[str]] = None

        # Filter issues by the type of the current assignee of this issue. Separate multiple values with commas. Possible values: Possible values: user, company, role, null. For Example: user.
        filterassigned_to_type: Optional[str] = None

        # Filter issues closed at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
        filterclosed_at: Optional[str] = None

        # Filter issues by the unique identifier of the user who closed the issue. Separate multiple values with commas. For Example: A3RGM375QTZ7.
        filterclosed_by: Optional[list[str]] = None

        # Filter issues created at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas
        filtercreated_at: Optional[str] = None

        # Filter issues by the unique identifier of the user who created the issue. Separate multiple values with commas.
        filtercreated_by: Optional[list[str]] = None

        # Filter issues by the custom attributes. Each custom attribute filter should be defined by it’s uuid. For example: filter[customAttributes][f227d940-ae9b-4722-9297-389f4411f010]=1,2,3. Separate multiple values with commas.
        filtercustom_attributes: Optional[list[str]] = None

        # Filter deleted issues. For example, filter[deleted]=true. If set to true it only returns deleted issues. If set to false it only returns undeleted issues. Note that we do not currently support returning both deleted and undeleted issues. Default value: false.
        filterdeleted: Optional[bool] = None

        # Filter issues by the chronological user-friendly identifier. Separate multiple values with commas.
        filterdisplay_id: Optional[int] = None

        # Filter issues by due date, in one of the following URL-encoded format: YYYY-MM-DD. Separate multiple values with commas.
        filterdue_date: Optional[str] = None

        # Filter issues by the unique issue ID. Separate multiple values with commas.
        filterid: Optional[list[str]] = None

        # Filter issues by the unique identifier of the type of the issue. Note that the API name for type is subtype. Separate multiple values with commas.
        filterissue_subtype_id: Optional[list[str]] = None

        # Filter issues by the unique identifier of the category of the issue. Note that the API name for category is type. Separate multiple values with commas.
        filterissue_type_id: Optional[list[str]] = None

        # Retrieves pushpin issues associated with the specified files. We support all file types that are compatible with the Files tool. You need to specify the URL-encoded file item IDs.
        filterlinked_document_urn: Optional[list[str]] = None

        # Retrieves issues associated with the specified location but not the location’s sublocations. To also retrieve issues that relate to the locations’s sublocations use the sublocationId filter. Separate multiple values with commas.
        filterlocation_id: Optional[list[str]] = None

        # Filter issues by the unique identifier of the type of root cause for the issue. Separate multiple values with commas.
        filterroot_cause_id: Optional[list[str]] = None

        # Filter issues using ‘search’ criteria. this will filter both title and issues display ID. For example, use filter[search]=300
        filtersearch: Optional[str] = None

        # Filter issues by start date, in one of the following URL-encoded format: YYYY-MM-DD. Separate multiple values with commas.
        filterstart_date: Optional[str] = None

        # Filter issues by their status. Separate multiple values with commas.
        filterstatus: Optional[str] = None

        # Retrieves issues associated with the specified unique LBS (Location Breakdown Structure) identifier, as well as issues associated with the sub locations of the LBS identifier. Separate multiple values with commas.
        filtersub_location_id: Optional[list[str]] = None

        # Filter issues updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas. 
        filterupdated_at: Optional[str] = None

        # Filter issues by the unique identifier of the user who updated the issue. Separate multiple values with commas.
        filterupdated_by: Optional[list[str]] = None

        # Only return valid issues (=no empty type/subtype). Default value: undefined (meaning will return both valid & invalid issues).
        filtervalid: Optional[bool] = None

        # Return specified number of issues. Acceptable values are 1-100. Default value: 100.
        limit: Optional[int] = None

        # Return issues starting from the specified offset number. Default value: 0.
        offset: Optional[int] = None

        # Sort issue comments by specified fields. Separate multiple values with commas. To sort in descending order add a - (minus sign) before the sort criteria
        sort_by: list[SortBy] = field(default_factory=list)

    
    @dataclass
    class IssuesRequestBuilderGetRequestConfiguration(RequestConfiguration[IssuesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IssuesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

