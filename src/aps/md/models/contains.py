from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Contains(AdditionalDataHolder, Parsable):
    """
    Use this to retrieve only the properties of objects where a specified property contains a specified value. 
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Returns only the objects where the value of the specified property contains the words specified in a string.The first element of the array contains the name of the property. The second element contains a string containing the words to match. The array can only be two elements long.For example, if you specify an array as: ``"$contains":["properties.Materials and Finishes.Structural Material","Concrete Situ"]``, the request returns the properties of all objects whose ``properties.Materials and Finishes.Structural Material`` property contains the words  ``Concrete`` and ``Situ``. You can specify up to 50 words.
    contains: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Contains:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Contains
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Contains()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "$contains": lambda n : setattr(self, 'contains', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("$contains", self.contains)
        writer.write_additional_data_value(self.additional_data)
    

