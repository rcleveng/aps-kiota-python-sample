from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Batchcompleteupload_object_requests(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of eTags. S3 returns an eTag to each upload request, be it for a chunk or an entire file. For a single-part upload, this array contains the expected eTag of the entire object. For a multipart upload, this array contains the expected eTag of each part of the upload; the index of an eTag in the array corresponds to its part number in the upload. If provided, OSS will validate these eTags against the content in S3, and return an error if the eTags do not match.
    e_tags: Optional[list[str]] = None
    # The URL-encoded human friendly name of the object for which to complete an upload.
    object_key: Optional[str] = None
    # The expected size of the object. If provided, OSS will check this against the object in S3 and return an error if the size does not match.
    size: Optional[int] = None
    # The ID uniquely identifying the upload session that was returned when you obtained the signed upload URL.
    upload_key: Optional[str] = None
    # The Cache-Control value for the uploaded object to record within OSS.
    x_ads_meta_cache_control: Optional[str] = None
    # The Content-Disposition value for the uploaded object to record within OSS.
    x_ads_meta_content_disposition: Optional[str] = None
    # The Content-Encoding value for the uploaded object to record within OSS.
    x_ads_meta_content_encoding: Optional[str] = None
    # The Content-Type value for the uploaded object to record within OSS.
    x_ads_meta_content_type: Optional[str] = None
    # Custom metadata to be stored with the object, which can be retrieved later on download or when retrieving object details. Must be a JSON object that is less than 100 bytes.
    x_ads_user_defined_metadata: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Batchcompleteupload_object_requests:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Batchcompleteupload_object_requests
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Batchcompleteupload_object_requests()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "eTags": lambda n : setattr(self, 'e_tags', n.get_collection_of_primitive_values(str)),
            "objectKey": lambda n : setattr(self, 'object_key', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "uploadKey": lambda n : setattr(self, 'upload_key', n.get_str_value()),
            "x-ads-meta-Cache-Control": lambda n : setattr(self, 'x_ads_meta_cache_control', n.get_str_value()),
            "x-ads-meta-Content-Disposition": lambda n : setattr(self, 'x_ads_meta_content_disposition', n.get_str_value()),
            "x-ads-meta-Content-Encoding": lambda n : setattr(self, 'x_ads_meta_content_encoding', n.get_str_value()),
            "x-ads-meta-Content-Type": lambda n : setattr(self, 'x_ads_meta_content_type', n.get_str_value()),
            "x-ads-user-defined-metadata": lambda n : setattr(self, 'x_ads_user_defined_metadata', n.get_str_value()),
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
        writer.write_str_value("objectKey", self.object_key)
        writer.write_int_value("size", self.size)
        writer.write_str_value("uploadKey", self.upload_key)
        writer.write_str_value("x-ads-meta-Cache-Control", self.x_ads_meta_cache_control)
        writer.write_str_value("x-ads-meta-Content-Disposition", self.x_ads_meta_content_disposition)
        writer.write_str_value("x-ads-meta-Content-Encoding", self.x_ads_meta_content_encoding)
        writer.write_str_value("x-ads-meta-Content-Type", self.x_ads_meta_content_type)
        writer.write_str_value("x-ads-user-defined-metadata", self.x_ads_user_defined_metadata)
        writer.write_additional_data_value(self.additional_data)
    

