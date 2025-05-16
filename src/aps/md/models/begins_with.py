from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BeginsWith(AdditionalDataHolder, Parsable):
    """
    Use this to retrieve only the properties of objects with names beginning with a specified string. 
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Returns only the objects with their ``name`` attribute beginning with the specified string.The first element of the array contains the name of the attribute to match (``name``). The second element contains the string to match. The array can have only two elements. Only the objects whose name begin with the specified string are returned.
    prefix: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BeginsWith:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BeginsWith
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BeginsWith()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "$prefix": lambda n : setattr(self, 'prefix', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("$prefix", self.prefix)
        writer.write_additional_data_value(self.additional_data)
    

