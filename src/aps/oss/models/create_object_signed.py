from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Create_object_signed(AdditionalDataHolder, Parsable):
    """
    The request payload for a Generate OSS Signed URL operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # IP addresses that can make a request to this URL.
    allowed_ip_addresses: Optional[list[str]] = None
    # Value for expiration in minutes
    expiration: Optional[int] = None
    # URL created for downloading the object
    signed_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Create_object_signed:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Create_object_signed
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Create_object_signed()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowedIpAddresses": lambda n : setattr(self, 'allowed_ip_addresses', n.get_collection_of_primitive_values(str)),
            "expiration": lambda n : setattr(self, 'expiration', n.get_int_value()),
            "signedUrl": lambda n : setattr(self, 'signed_url', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("allowedIpAddresses", self.allowed_ip_addresses)
        writer.write_int_value("expiration", self.expiration)
        writer.write_str_value("signedUrl", self.signed_url)
        writer.write_additional_data_value(self.additional_data)
    

