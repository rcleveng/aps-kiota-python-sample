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
    from .........models.relationship_links import RelationshipLinks
    from .........models.relationship_links400_error import RelationshipLinks400Error
    from .........models.relationship_links403_error import RelationshipLinks403Error
    from .........models.relationship_links404_error import RelationshipLinks404Error

class LinksRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/folders/{folder_id}/relationships/links
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LinksRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/folders/{folder_id}/relationships/links", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RelationshipLinks]:
        """
        Returns a list of links for the specified folder. Custom relationships can be established between a folder and other external resources residing outside the data domain service. A link’s ``href`` attribute defines the target URI to access a resource.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RelationshipLinks]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.relationship_links400_error import RelationshipLinks400Error
        from .........models.relationship_links403_error import RelationshipLinks403Error
        from .........models.relationship_links404_error import RelationshipLinks404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": RelationshipLinks400Error,
            "403": RelationshipLinks403Error,
            "404": RelationshipLinks404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.relationship_links import RelationshipLinks

        return await self.request_adapter.send_async(request_info, RelationshipLinks, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of links for the specified folder. Custom relationships can be established between a folder and other external resources residing outside the data domain service. A link’s ``href`` attribute defines the target URI to access a resource.**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/). 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> LinksRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LinksRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LinksRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LinksRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

