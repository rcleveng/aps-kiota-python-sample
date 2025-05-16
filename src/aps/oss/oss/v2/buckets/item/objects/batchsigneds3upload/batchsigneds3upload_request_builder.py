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
    from .......models.batchsigneds3upload_object import Batchsigneds3upload_object
    from .......models.batchsigneds3upload_response import Batchsigneds3upload_response

class Batchsigneds3uploadRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/buckets/{bucketKey}/objects/batchsigneds3upload
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new Batchsigneds3uploadRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/buckets/{bucketKey}/objects/batchsigneds3upload{?minutesExpiration*,useAcceleration*}", path_parameters)
    
    async def post(self,body: Batchsigneds3upload_object, request_configuration: Optional[RequestConfiguration[Batchsigneds3uploadRequestBuilderPostQueryParameters]] = None) -> Optional[Batchsigneds3upload_response]:
        """
        Creates and returns signed URLs to upload a set of objects directly to S3. These signed URLs expire in 2 minutes by default, but you can change this duration if needed.  You must start uploading the objects before the signed URLs expire. The upload  itself can take longer.Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.If required, you can request an array of signed URLs for each object, which lets you upload the objects in chunks. Once you upload all chunks you must call the [Complete Batch Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-batchcompleteupload-POST/) operation to indicate completion. This instructs OSS to assemble the chunks and reconstitute the object on OSS. You must call this operation even if you requested a single signed URL for an object.If an upload fails after the validity period of a signed URL has elapsed, you can call this operation again to obtain fresh signed URLs. However, you must use the same ``uploadKey`` that was returned when you originally called this operation. 
        param body: The request payload for a Batch Generate Signed S3 Upload URLs operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Batchsigneds3upload_response]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.batchsigneds3upload_response import Batchsigneds3upload_response

        return await self.request_adapter.send_async(request_info, Batchsigneds3upload_response, None)
    
    def to_post_request_information(self,body: Batchsigneds3upload_object, request_configuration: Optional[RequestConfiguration[Batchsigneds3uploadRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates and returns signed URLs to upload a set of objects directly to S3. These signed URLs expire in 2 minutes by default, but you can change this duration if needed.  You must start uploading the objects before the signed URLs expire. The upload  itself can take longer.Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.If required, you can request an array of signed URLs for each object, which lets you upload the objects in chunks. Once you upload all chunks you must call the [Complete Batch Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-batchcompleteupload-POST/) operation to indicate completion. This instructs OSS to assemble the chunks and reconstitute the object on OSS. You must call this operation even if you requested a single signed URL for an object.If an upload fails after the validity period of a signed URL has elapsed, you can call this operation again to obtain fresh signed URLs. However, you must use the same ``uploadKey`` that was returned when you originally called this operation. 
        param body: The request payload for a Batch Generate Signed S3 Upload URLs operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, application/vnd.api+json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> Batchsigneds3uploadRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Batchsigneds3uploadRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return Batchsigneds3uploadRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class Batchsigneds3uploadRequestBuilderPostQueryParameters():
        """
        Creates and returns signed URLs to upload a set of objects directly to S3. These signed URLs expire in 2 minutes by default, but you can change this duration if needed.  You must start uploading the objects before the signed URLs expire. The upload  itself can take longer.Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.If required, you can request an array of signed URLs for each object, which lets you upload the objects in chunks. Once you upload all chunks you must call the [Complete Batch Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-batchcompleteupload-POST/) operation to indicate completion. This instructs OSS to assemble the chunks and reconstitute the object on OSS. You must call this operation even if you requested a single signed URL for an object.If an upload fails after the validity period of a signed URL has elapsed, you can call this operation again to obtain fresh signed URLs. However, you must use the same ``uploadKey`` that was returned when you originally called this operation. 
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
                return "minutesExpiration"
            if original_name == "use_acceleration":
                return "useAcceleration"
            return original_name
        
        # The time window (in minutes) the signed URL will remain usable. Acceptable values = 1-60 minutes. Default = 2 minutes.**Tip:** Use the smallest possible time window to minimize exposure of the signed URL.
        minutes_expiration: Optional[int] = None

        # ``true`` : (Default) Generates a faster S3 signed URL using Transfer Acceleration.``false``: Generates a standard S3 signed URL.
        use_acceleration: Optional[bool] = None

    
    @dataclass
    class Batchsigneds3uploadRequestBuilderPostRequestConfiguration(RequestConfiguration[Batchsigneds3uploadRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

