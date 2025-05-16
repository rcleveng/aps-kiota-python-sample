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
    from .....models.object_details import ObjectDetails
    from .....models.reason import Reason
    from .....models.region import Region
    from .resumable.resumable_request_builder import ResumableRequestBuilder
    from .with_hash_put_request_body import WithHashPutRequestBody

class WithHashItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/signedresources/{hash}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithHashItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/signedresources/{hash}{?region*,response%2Dcontent%2Ddisposition*,response%2Dcontent%2Dtype*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Delete an object using an OSS signed URL to access it.Only applications that own the bucket containing the object can call this operation. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithHashItemRequestBuilderGetQueryParameters]] = None) -> Optional[bytes]:
        """
        Downloads an object using an OSS signed URL.**Note:** The signed URL returned by [Generate OSS Signed URL](/en/docs/data/v2/reference/http/signedresources-:id-GET/)  contains the ``hash`` URI parameter as well. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    async def put(self,body: WithHashPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ObjectDetails]:
        """
        Replaces an object that already exists on OSS, using an OSS signed URL. The signed URL must fulfil the following conditions:- The signed URL is valid (it has not expired as yet).- It was generated with ``write`` or ``readwrite`` for the ``access`` parameter.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ObjectDetails]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.reason import Reason

        error_mapping: dict[str, type[ParsableFactory]] = {
            "412": Reason,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.object_details import ObjectDetails

        return await self.request_adapter.send_async(request_info, ObjectDetails, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete an object using an OSS signed URL to access it.Only applications that own the bucket containing the object can call this operation. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithHashItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Downloads an object using an OSS signed URL.**Note:** The signed URL returned by [Generate OSS Signed URL](/en/docs/data/v2/reference/http/signedresources-:id-GET/)  contains the ``hash`` URI parameter as well. 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/octet-stream")
        return request_info
    
    def to_put_request_information(self,body: WithHashPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Replaces an object that already exists on OSS, using an OSS signed URL. The signed URL must fulfil the following conditions:- The signed URL is valid (it has not expired as yet).- It was generated with ``write`` or ``readwrite`` for the ``access`` parameter.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, application/vnd.api+json")
        request_info.set_content_from_parsable(self.request_adapter, "application/x-www-form-urlencoded", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WithHashItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithHashItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithHashItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def resumable(self) -> ResumableRequestBuilder:
        """
        The resumable property
        """
        from .resumable.resumable_request_builder import ResumableRequestBuilder

        return ResumableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithHashItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithHashItemRequestBuilderGetQueryParameters():
        """
        Downloads an object using an OSS signed URL.**Note:** The signed URL returned by [Generate OSS Signed URL](/en/docs/data/v2/reference/http/signedresources-:id-GET/)  contains the ``hash`` URI parameter as well. 
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "response_content_disposition":
                return "response%2Dcontent%2Ddisposition"
            if original_name == "response_content_type":
                return "response%2Dcontent%2Dtype"
            if original_name == "region":
                return "region"
            return original_name
        
        # Specifies where the bucket containing the object stored. Possible values are:- ``US`` - (Default) Data center for the US region.- ``EMEA`` - Data center for the European Union, Middle East, and Africa.- ``APAC`` -  (Beta) Data center for Australia.**Note:** Beta features are subject to change. Please do not use in production environments.
        region: Optional[Region] = None

        # The value of the Content-Disposition header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Disposition header defaults to the value stored with OSS.
        response_content_disposition: Optional[str] = None

        # The value of the Content-Type header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Type header defaults to the value stored with OSS.
        response_content_type: Optional[str] = None

    
    @dataclass
    class WithHashItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithHashItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithHashItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

