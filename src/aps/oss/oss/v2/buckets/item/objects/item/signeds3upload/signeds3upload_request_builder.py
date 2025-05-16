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
    from ........models.completes3upload_body import Completes3upload_body
    from ........models.signeds3upload_response import Signeds3upload_response

class Signeds3uploadRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3upload
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new Signeds3uploadRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3upload{?firstPart*,minutesExpiration*,parts*,uploadKey*,useAcceleration*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[Signeds3uploadRequestBuilderGetQueryParameters]] = None) -> Optional[Signeds3upload_response]:
        """
        Gets a signed URL to upload an object directly to S3, bypassing OSS servers. You can also request an array of signed URLs which lets you upload an object in chunks.This signed URL expires in 2 minutes by default, but you can change this duration if needed.  You must start the upload before the signed URL expires. The upload itself can take longer. If the upload fails after the validity period of the signed URL has elapsed, you can call this operation again to obtain a fresh signed URL (or an array of signed URLs as the case may be). However, you must use the same ``uploadKey`` that was returned when you originally called this operation. Only applications that own the bucket can call this operation.**Note:** Once you upload all chunks you must call the [Complete Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST/) operation to indicate completion. This instructs OSS to assemble the chunks and reconstitute the object on OSS. You must call this operation even when using a single signed URL. In addition to this operation that generates S3 signed URLs, OSS provides an operation to generate OSS signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.    
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Signeds3upload_response]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.signeds3upload_response import Signeds3upload_response

        return await self.request_adapter.send_async(request_info, Signeds3upload_response, None)
    
    async def post(self,body: Completes3upload_body, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Requests OSS to assemble and reconstitute the object that was uploaded using signed S3 upload URL. You must call this operation only after all parts/chunks of the object has been uploaded.
        param body: The request payload for a Complete Upload to S3 Signed URL operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[Signeds3uploadRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets a signed URL to upload an object directly to S3, bypassing OSS servers. You can also request an array of signed URLs which lets you upload an object in chunks.This signed URL expires in 2 minutes by default, but you can change this duration if needed.  You must start the upload before the signed URL expires. The upload itself can take longer. If the upload fails after the validity period of the signed URL has elapsed, you can call this operation again to obtain a fresh signed URL (or an array of signed URLs as the case may be). However, you must use the same ``uploadKey`` that was returned when you originally called this operation. Only applications that own the bucket can call this operation.**Note:** Once you upload all chunks you must call the [Complete Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST/) operation to indicate completion. This instructs OSS to assemble the chunks and reconstitute the object on OSS. You must call this operation even when using a single signed URL. In addition to this operation that generates S3 signed URLs, OSS provides an operation to generate OSS signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.    
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, application/vnd.api+json")
        return request_info
    
    def to_post_request_information(self,body: Completes3upload_body, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Requests OSS to assemble and reconstitute the object that was uploaded using signed S3 upload URL. You must call this operation only after all parts/chunks of the object has been uploaded.
        param body: The request payload for a Complete Upload to S3 Signed URL operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> Signeds3uploadRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Signeds3uploadRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return Signeds3uploadRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class Signeds3uploadRequestBuilderGetQueryParameters():
        """
        Gets a signed URL to upload an object directly to S3, bypassing OSS servers. You can also request an array of signed URLs which lets you upload an object in chunks.This signed URL expires in 2 minutes by default, but you can change this duration if needed.  You must start the upload before the signed URL expires. The upload itself can take longer. If the upload fails after the validity period of the signed URL has elapsed, you can call this operation again to obtain a fresh signed URL (or an array of signed URLs as the case may be). However, you must use the same ``uploadKey`` that was returned when you originally called this operation. Only applications that own the bucket can call this operation.**Note:** Once you upload all chunks you must call the [Complete Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST/) operation to indicate completion. This instructs OSS to assemble the chunks and reconstitute the object on OSS. You must call this operation even when using a single signed URL. In addition to this operation that generates S3 signed URLs, OSS provides an operation to generate OSS signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.    
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "first_part":
                return "firstPart"
            if original_name == "minutes_expiration":
                return "minutesExpiration"
            if original_name == "upload_key":
                return "uploadKey"
            if original_name == "use_acceleration":
                return "useAcceleration"
            if original_name == "parts":
                return "parts"
            return original_name
        
        # The index of the first chunk to be uploaded.
        first_part: Optional[int] = None

        # The time window (in minutes) the signed URL will remain usable. Acceptable values = 1-60 minutes. Default = 2 minutes.**Tip:** Use the smallest possible time window to minimize exposure of the signed URL.
        minutes_expiration: Optional[int] = None

        # The number of parts you intend to chunk the object for uploading. OSS will return that many signed URLs, one URL for each chunk. If you do not specify a value you'll get only one URL to upload the entire object.             
        parts: Optional[int] = None

        # The ``uploadKey`` of a previously-initiated upload, in order to request more chunk upload URLs for the same upload. If you do not specify a value, OSS will initiate a new upload entirely.
        upload_key: Optional[str] = None

        # ``true`` : (Default) Generates a faster S3 signed URL using Transfer Acceleration.``false``: Generates a standard S3 signed URL.
        use_acceleration: Optional[bool] = None

    
    @dataclass
    class Signeds3uploadRequestBuilderGetRequestConfiguration(RequestConfiguration[Signeds3uploadRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class Signeds3uploadRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

