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
    from .....models.job import Job
    from .....models.job_payload import JobPayload

class JobRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata/job
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new JobRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata/job", path_parameters)
    
    async def post(self,body: JobPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Job]:
        """
        Creates a job to translate the specified source design to another format, generating derivatives of the source design. You can optionally:- Extract selected parts of a design and export the set of geometries in OBJ format.- Generate different-sized thumbnails.When the translation job runs, details about the process and generated derivatives are logged to a JSON file known as a manifest. This manifest is typically created during the first translation of a source design. Subsequently, the system updates the same manifest whenever a translation is performed for that design. If necessary, you can set the ``x-ads-force`` parameter to ``true``. Then, the system will delete the existing manifest and create a new one. However, be aware that doing so will also delete all previously generated derivatives.
        param body: An object that represents the request body of a Create Translation Job operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Job]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.job import Job

        return await self.request_adapter.send_async(request_info, Job, None)
    
    def to_post_request_information(self,body: JobPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a job to translate the specified source design to another format, generating derivatives of the source design. You can optionally:- Extract selected parts of a design and export the set of geometries in OBJ format.- Generate different-sized thumbnails.When the translation job runs, details about the process and generated derivatives are logged to a JSON file known as a manifest. This manifest is typically created during the first translation of a source design. Subsequently, the system updates the same manifest whenever a translation is performed for that design. If necessary, you can set the ``x-ads-force`` parameter to ``true``. Then, the system will delete the existing manifest and create a new one. However, be aware that doing so will also delete all previously generated derivatives.
        param body: An object that represents the request body of a Create Translation Job operation.
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
    
    def with_url(self,raw_url: str) -> JobRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: JobRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return JobRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class JobRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

