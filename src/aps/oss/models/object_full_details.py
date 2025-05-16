from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ObjectFullDetails(AdditionalDataHolder, Parsable):
    """
    Represents detailed information about an object within a bucket.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The bucket key of the bucket that contains the object.
    bucket_key: Optional[str] = None
    # The format of the data stored within the object, expressed as a MIME type.
    content_type: Optional[str] = None
    # The time the object was created, represented as a Unix timestamp. Only returned if explicitly requested using the ``with`` query string parameter.
    created_date: Optional[int] = None
    # The time the object was last accessed, represented as a Unix timestamp. Only returned if explicitly requested using the ``with`` query string parameter.
    last_accessed_date: Optional[int] = None
    # The time the object was most recently modified, represented as a Unix timestamp. Only returned if explicitly requested using the ``with`` query string parameter.
    last_modified_date: Optional[int] = None
    # A URL that points to the actual location of the object.
    location: Optional[str] = None
    # An identifier (URN) that uniquely and persistently identifies the object.
    object_id: Optional[str] = None
    # A URL-encoded human friendly name to identify the object.
    object_key: Optional[str] = None
    # A hash value computed from the data of the object.
    sha1: Optional[bytes] = None
    # The total amount of storage space occupied by the object, in bytes.
    size: Optional[int] = None
    # Any custom metadata, if available. Only returned if explicitly requested for using the ``with`` query string parameter.
    user_defined_metadata: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ObjectFullDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ObjectFullDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ObjectFullDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bucketKey": lambda n : setattr(self, 'bucket_key', n.get_str_value()),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "createdDate": lambda n : setattr(self, 'created_date', n.get_int_value()),
            "lastAccessedDate": lambda n : setattr(self, 'last_accessed_date', n.get_int_value()),
            "lastModifiedDate": lambda n : setattr(self, 'last_modified_date', n.get_int_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "objectKey": lambda n : setattr(self, 'object_key', n.get_str_value()),
            "sha1": lambda n : setattr(self, 'sha1', n.get_bytes_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "userDefinedMetadata": lambda n : setattr(self, 'user_defined_metadata', n.get_str_value()),
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
        writer.write_str_value("bucketKey", self.bucket_key)
        writer.write_str_value("contentType", self.content_type)
        writer.write_int_value("createdDate", self.created_date)
        writer.write_int_value("lastAccessedDate", self.last_accessed_date)
        writer.write_int_value("lastModifiedDate", self.last_modified_date)
        writer.write_str_value("location", self.location)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("objectKey", self.object_key)
        writer.write_bytes_value("sha1", self.sha1)
        writer.write_int_value("size", self.size)
        writer.write_str_value("userDefinedMetadata", self.user_defined_metadata)
        writer.write_additional_data_value(self.additional_data)
    

