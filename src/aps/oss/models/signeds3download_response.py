from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .download_status import Download_status
    from .signeds3download_response_params import Signeds3download_response_params
    from .signeds3download_response_urls import Signeds3download_response_urls

@dataclass
class Signeds3download_response(AdditionalDataHolder, Parsable):
    """
    An object representing the response payload on successful execution of a Generate Signed S3 Download URL operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The values that were requested for the following parameters when requesting the S3 signed URL.- ``Content-Type``- ``Content-Disposition``- ``Cache-Control``.
    params: Optional[Signeds3download_response_params] = None
    # A hash value computed from the data of the object, if available.
    sha1: Optional[str] = None
    # The total amount of storage space occupied by the object, in bytes.
    size: Optional[int] = None
    # Indicates the upload status of the requested object. Possible values are:- ``complete`` - The upload process is finished. If the object was uploaded in chunks, assembly of chunks into the final object is also complete.- ``chunked`` - The object was uploaded in chunks, but assembly of chunks into the final object is still pending. `public-resource-fallback`` = ``false``- ``fallback`` - The object was uploaded in chunks, but assembly of chunks into the final object is still pending. `public-resource-fallback`` = ``true`` 
    status: Optional[Download_status] = None
    # A S3 signed URL with which to download the object. This attribute is returned when ``status`` is ``complete`` or ``fallback``; in the latter case, this will return an OSS signed URL, not an S3 signed URL.
    url: Optional[str] = None
    # A map of S3 signed URLs, one for each chunk of an unmerged resumable upload. This attribute is returned when ``status`` is ``chunked``. The key of each entry is the byte range of the total file which the chunk comprises.
    urls: Optional[Signeds3download_response_urls] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Signeds3download_response:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Signeds3download_response
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Signeds3download_response()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .download_status import Download_status
        from .signeds3download_response_params import Signeds3download_response_params
        from .signeds3download_response_urls import Signeds3download_response_urls

        from .download_status import Download_status
        from .signeds3download_response_params import Signeds3download_response_params
        from .signeds3download_response_urls import Signeds3download_response_urls

        fields: dict[str, Callable[[Any], None]] = {
            "params": lambda n : setattr(self, 'params', n.get_object_value(Signeds3download_response_params)),
            "sha1": lambda n : setattr(self, 'sha1', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Download_status)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
            "urls": lambda n : setattr(self, 'urls', n.get_object_value(Signeds3download_response_urls)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("params", self.params)
        writer.write_str_value("sha1", self.sha1)
        writer.write_int_value("size", self.size)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("url", self.url)
        writer.write_object_value("urls", self.urls)
        writer.write_additional_data_value(self.additional_data)
    

