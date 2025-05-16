from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .properties_data_collection import Properties_data_collection

@dataclass
class Properties_data(AdditionalDataHolder, Parsable):
    """
    An envelope that encapsulates the return data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A non-hierarchical list of objects contained in the specified Model View. Each object has a ``properties`` attribute, which contains the properties of that object.
    collection: Optional[list[Properties_data_collection]] = None
    # The type of data that is returned. Always ``properties``.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Properties_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Properties_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Properties_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .properties_data_collection import Properties_data_collection

        from .properties_data_collection import Properties_data_collection

        fields: dict[str, Callable[[Any], None]] = {
            "collection": lambda n : setattr(self, 'collection', n.get_collection_of_object_values(Properties_data_collection)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_collection_of_object_values("collection", self.collection)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

