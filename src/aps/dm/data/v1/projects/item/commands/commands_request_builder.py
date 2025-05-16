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
    from ......models.command import Command
    from ......models.command400_error import Command400Error
    from ......models.command403_error import Command403Error
    from ......models.command404_error import Command404Error
    from ......models.command_payload import CommandPayload

class CommandsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /data/v1/projects/{project_id}/commands
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CommandsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/data/v1/projects/{project_id}/commands", path_parameters)
    
    async def post(self,body: CommandPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Command]:
        """
        Executes the command that you specify in the request body. Commands enable you to perform general operations on multiple resources.For example, you can check whether a user has permission to delete a collection of versions, items, and folders.The command as well as the input data for the command are specified using the ``data`` object of the request body. For more information about commands see the [Commands](/en/docs/data/v2/overview/commands/) section in the Developer's Guide.
        param body: Command Payload
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Command]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.command400_error import Command400Error
        from ......models.command403_error import Command403Error
        from ......models.command404_error import Command404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Command400Error,
            "403": Command403Error,
            "404": Command404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.command import Command

        return await self.request_adapter.send_async(request_info, Command, error_mapping)
    
    def to_post_request_information(self,body: CommandPayload, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Executes the command that you specify in the request body. Commands enable you to perform general operations on multiple resources.For example, you can check whether a user has permission to delete a collection of versions, items, and folders.The command as well as the input data for the command are specified using the ``data`` object of the request body. For more information about commands see the [Commands](/en/docs/data/v2/overview/commands/) section in the Developer's Guide.
        param body: Command Payload
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/vnd.api+json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CommandsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CommandsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CommandsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CommandsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

