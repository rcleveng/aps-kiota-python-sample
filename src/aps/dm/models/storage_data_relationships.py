from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .storage_data_relationships_target import Storage_data_relationships_target

@dataclass
class Storage_data_relationships(AdditionalDataHolder, Parsable):
    """
    Contains links to resources that are directly related to the storage location.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Information about the target object.
    target: Optional[Storage_data_relationships_target] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Storage_data_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Storage_data_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Storage_data_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .storage_data_relationships_target import Storage_data_relationships_target

        from .storage_data_relationships_target import Storage_data_relationships_target

        fields: dict[str, Callable[[Any], None]] = {
            "target": lambda n : setattr(self, 'target', n.get_object_value(Storage_data_relationships_target)),
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
        writer.write_object_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

