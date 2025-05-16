from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Completes3upload_body(AdditionalDataHolder, Parsable):
    """
    The request payload for a Complete Upload to S3 Signed URL operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of eTags. S3 returns an eTag to each upload request, be it for a chunk or an entire file. For a single-part upload, this array contains the expected eTag of the entire object. For a multipart upload, this array contains the expected eTag of each part of the upload; the index of an eTag in the array corresponds to its part number in the upload. If provided, OSS will validate these eTags against the content in S3, and return an error if the eTags do not match.
    e_tags: Optional[list[str]] = None
    # The expected size of the object. If provided, OSS will check this against the object in S3 and return an error if the size does not match.
    size: Optional[int] = None
    # The ID uniquely identifying the upload session that was returned when you called [Get S3 Signed Upload URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST/).
    upload_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Completes3upload_body:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Completes3upload_body
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Completes3upload_body()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "eTags": lambda n : setattr(self, 'e_tags', n.get_collection_of_primitive_values(str)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "uploadKey": lambda n : setattr(self, 'upload_key', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("eTags", self.e_tags)
        writer.write_int_value("size", self.size)
        writer.write_str_value("uploadKey", self.upload_key)
        writer.write_additional_data_value(self.additional_data)
    

