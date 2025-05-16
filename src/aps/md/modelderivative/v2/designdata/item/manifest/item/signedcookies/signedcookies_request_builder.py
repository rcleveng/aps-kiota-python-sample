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
    from ........models.derivative_download import DerivativeDownload

class SignedcookiesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}/signedcookies
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SignedcookiesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}/signedcookies{?minutes%2Dexpiration*,response%2Dcontent%2Ddisposition*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SignedcookiesRequestBuilderGetQueryParameters]] = None) -> Optional[DerivativeDownload]:
        """
        Returns a download URL and a set of signed cookies, which lets you securely download the derivative specified by the ``derivativeUrn`` URI parameter. The signed cookies have a lifetime of 6 hours. You can use range headers with the returned download URL to download the derivative in chunks, in parallel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DerivativeDownload]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.derivative_download import DerivativeDownload

        return await self.request_adapter.send_async(request_info, DerivativeDownload, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SignedcookiesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a download URL and a set of signed cookies, which lets you securely download the derivative specified by the ``derivativeUrn`` URI parameter. The signed cookies have a lifetime of 6 hours. You can use range headers with the returned download URL to download the derivative in chunks, in parallel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> SignedcookiesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SignedcookiesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SignedcookiesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SignedcookiesRequestBuilderGetQueryParameters():
        """
        Returns a download URL and a set of signed cookies, which lets you securely download the derivative specified by the ``derivativeUrn`` URI parameter. The signed cookies have a lifetime of 6 hours. You can use range headers with the returned download URL to download the derivative in chunks, in parallel.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "minutes_expiration":
                return "minutes%2Dexpiration"
            if original_name == "response_content_disposition":
                return "response%2Dcontent%2Ddisposition"
            return original_name
        
        # Specifies how many minutes the signed cookies should remain valid. Default value is 360 minutes. The value you specify must be lower than the default value for this parameter. If you specify a value greater than the default value, the Model Derivative service will return an error with an HTTP status code of ``400``.
        minutes_expiration: Optional[int] = None

        # The value that must be specified as the ``response-content-disposition`` query string parameter with the download URL. Must begin with ``attachment``. This value defaults to the default value corresponding to the derivative/file.
        response_content_disposition: Optional[str] = None

    
    @dataclass
    class SignedcookiesRequestBuilderGetRequestConfiguration(RequestConfiguration[SignedcookiesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

