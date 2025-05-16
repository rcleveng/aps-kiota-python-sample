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
    from ......models.bucket_objects import Bucket_objects
    from .batchcompleteupload.batchcompleteupload_request_builder import BatchcompleteuploadRequestBuilder
    from .batchsigneds3download.batchsigneds3download_request_builder import Batchsigneds3downloadRequestBuilder
    from .batchsigneds3upload.batchsigneds3upload_request_builder import Batchsigneds3uploadRequestBuilder
    from .item.with_object_key_item_request_builder import WithObjectKeyItemRequestBuilder

class ObjectsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/buckets/{bucketKey}/objects
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ObjectsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/buckets/{bucketKey}/objects{?beginsWith*,limit*,startAt*}", path_parameters)
    
    def by_object_key(self,object_key: str) -> WithObjectKeyItemRequestBuilder:
        """
        Gets an item from the ApiSdk.oss.v2.buckets.item.objects.item collection
        param object_key: The URL-encoded human friendly name of the object.
        Returns: WithObjectKeyItemRequestBuilder
        """
        if object_key is None:
            raise TypeError("object_key cannot be null.")
        from .item.with_object_key_item_request_builder import WithObjectKeyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["objectKey"] = object_key
        return WithObjectKeyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ObjectsRequestBuilderGetQueryParameters]] = None) -> Optional[Bucket_objects]:
        """
        Returns a list objects in the specified bucket. Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Bucket_objects]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.bucket_objects import Bucket_objects

        return await self.request_adapter.send_async(request_info, Bucket_objects, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ObjectsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list objects in the specified bucket. Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, application/vnd.api+json")
        return request_info
    
    def with_url(self,raw_url: str) -> ObjectsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ObjectsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ObjectsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def batchcompleteupload(self) -> BatchcompleteuploadRequestBuilder:
        """
        The batchcompleteupload property
        """
        from .batchcompleteupload.batchcompleteupload_request_builder import BatchcompleteuploadRequestBuilder

        return BatchcompleteuploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def batchsigneds3download(self) -> Batchsigneds3downloadRequestBuilder:
        """
        The batchsigneds3download property
        """
        from .batchsigneds3download.batchsigneds3download_request_builder import Batchsigneds3downloadRequestBuilder

        return Batchsigneds3downloadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def batchsigneds3upload(self) -> Batchsigneds3uploadRequestBuilder:
        """
        The batchsigneds3upload property
        """
        from .batchsigneds3upload.batchsigneds3upload_request_builder import Batchsigneds3uploadRequestBuilder

        return Batchsigneds3uploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ObjectsRequestBuilderGetQueryParameters():
        """
        Returns a list objects in the specified bucket. Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "begins_with":
                return "beginsWith"
            if original_name == "start_at":
                return "startAt"
            if original_name == "limit":
                return "limit"
            return original_name
        
        # Filters the results by the value you specify. Only the objects with their ``objectKey`` beginning with the specified string are returned.
        begins_with: Optional[str] = None

        # The number of items you want per page.Acceptable values = 1-100. Default = 10.
        limit: Optional[int] = None

        # The ID of the last item that was returned in the previous result set.  It enables the system to return subsequent items starting from the next one after the specified ID.
        start_at: Optional[str] = None

    
    @dataclass
    class ObjectsRequestBuilderGetRequestConfiguration(RequestConfiguration[ObjectsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

