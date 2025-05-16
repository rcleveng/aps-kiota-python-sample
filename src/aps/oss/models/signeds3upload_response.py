from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Signeds3upload_response(AdditionalDataHolder, Parsable):
    """
    The response payload to a Generate Signed S3 Upload URL operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The deadline to call [Complete Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST/) for the object. If not completed by this time, all uploaded data for this session will be discarded.
    upload_expiration: Optional[str] = None
    # An ID that uniquely identifies the upload session. It allows OSS to differentiate between fresh upload attempts from attempts to resume uploading data for an active upload session, in case of network interruptions. You must provide this value when:- Re-requesting chunk URLs for an active upload session. - When calling the [Complete Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST/) operation to end an active upload session.
    upload_key: Optional[str] = None
    # The date and time, in the ISO 8601 format, indicating when the signed URLs will expire.
    url_expiration: Optional[str] = None
    # An array of signed URLs. For a single-part upload, this will contain only one URL. For a multipart upload, there will be one for each chunk of a multipart upload; the index of the URL in the array corresponds to the part number of the chunk.
    urls: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Signeds3upload_response:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Signeds3upload_response
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Signeds3upload_response()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "uploadExpiration": lambda n : setattr(self, 'upload_expiration', n.get_str_value()),
            "uploadKey": lambda n : setattr(self, 'upload_key', n.get_str_value()),
            "urlExpiration": lambda n : setattr(self, 'url_expiration', n.get_str_value()),
            "urls": lambda n : setattr(self, 'urls', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("uploadExpiration", self.upload_expiration)
        writer.write_str_value("uploadKey", self.upload_key)
        writer.write_str_value("urlExpiration", self.url_expiration)
        writer.write_collection_of_primitive_values("urls", self.urls)
        writer.write_additional_data_value(self.additional_data)
    

