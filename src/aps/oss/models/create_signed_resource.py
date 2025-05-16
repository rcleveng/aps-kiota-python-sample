from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Create_signed_resource(AdditionalDataHolder, Parsable):
    """
    The request payload for a Generate OSS Signed URL operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The time window (in minutes) the signed URL will remain usable. Acceptable values = 1-60 minutes. Default = 2 minutes.**Tip:** Use the smallest possible time window to minimize exposure of the signed URL.
    minutes_expiration: Optional[int] = None
    # ``true`` : The signed URL will expire immediately after use. For example, when downloading an object, URL will expire once the download is complete.``false`` : (Default) The signed URL will remain usable for the entire time window specified by ``minutesExpiration``. 
    single_use: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Create_signed_resource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Create_signed_resource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Create_signed_resource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "minutesExpiration": lambda n : setattr(self, 'minutes_expiration', n.get_int_value()),
            "singleUse": lambda n : setattr(self, 'single_use', n.get_bool_value()),
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
        writer.write_int_value("minutesExpiration", self.minutes_expiration)
        writer.write_bool_value("singleUse", self.single_use)
        writer.write_additional_data_value(self.additional_data)
    

