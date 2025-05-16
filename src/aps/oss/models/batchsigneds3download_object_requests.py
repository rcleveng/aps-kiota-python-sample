from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Batchsigneds3download_object_requests(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A timestamp in the HTTP date format (Mon, DD Month YYYY HH:MM:SS GMT). A signed URL is returned only if the object has been modified since the specified timestamp. If not, a 304 (Not Modified) HTTP status is returned.
    if_modified_since: Optional[str] = None
    # The last known ETag value of the object. OSS returns the signed URL only if the ``If-None-Match`` header differs from the ETag value of the object on S3. If not, it returns a 304 "Not Modified" HTTP status.
    if_none_match: Optional[str] = None
    # The URL-encoded human friendly name of the object to download.
    object_key: Optional[str] = None
    # The value of the Cache-Control header you want to receive when you download the object using the signed URL. If you do not specify a value, the Cache-Control header defaults to the value stored with OSS.
    response_cache_control: Optional[str] = None
    # The value of the Content-Disposition header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Disposition header defaults to the value stored with OSS.
    response_content_disposition: Optional[str] = None
    # The value of the Content-Type header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Type header defaults to the value stored with OSS.
    response_content_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Batchsigneds3download_object_requests:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Batchsigneds3download_object_requests
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Batchsigneds3download_object_requests()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "If-Modified-Since": lambda n : setattr(self, 'if_modified_since', n.get_str_value()),
            "If-None-Match": lambda n : setattr(self, 'if_none_match', n.get_str_value()),
            "objectKey": lambda n : setattr(self, 'object_key', n.get_str_value()),
            "response-cache-control": lambda n : setattr(self, 'response_cache_control', n.get_str_value()),
            "response-content-disposition": lambda n : setattr(self, 'response_content_disposition', n.get_str_value()),
            "response-content-type": lambda n : setattr(self, 'response_content_type', n.get_str_value()),
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
        writer.write_str_value("If-Modified-Since", self.if_modified_since)
        writer.write_str_value("If-None-Match", self.if_none_match)
        writer.write_str_value("objectKey", self.object_key)
        writer.write_str_value("response-cache-control", self.response_cache_control)
        writer.write_str_value("response-content-disposition", self.response_content_disposition)
        writer.write_str_value("response-content-type", self.response_content_type)
        writer.write_additional_data_value(self.additional_data)
    

