from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DerivativeDownload(AdditionalDataHolder, Parsable):
    """
    An object that represents the successful response of a Fetch Derivative Download operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The content type of the derivative/file.
    content_type: Optional[str] = None
    # The calculated ETag hash of the derivative/file, if available.
    etag: Optional[str] = None
    # The 13-digit epoch time stamp indicating the time the signed cookies expire.
    expiration: Optional[float] = None
    # The size of the derivative/file, in bytes.
    size: Optional[float] = None
    # The download URL.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DerivativeDownload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DerivativeDownload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DerivativeDownload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "content-type": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "etag": lambda n : setattr(self, 'etag', n.get_str_value()),
            "expiration": lambda n : setattr(self, 'expiration', n.get_float_value()),
            "size": lambda n : setattr(self, 'size', n.get_float_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("content-type", self.content_type)
        writer.write_str_value("etag", self.etag)
        writer.write_float_value("expiration", self.expiration)
        writer.write_float_value("size", self.size)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

