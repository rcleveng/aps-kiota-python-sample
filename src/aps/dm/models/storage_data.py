from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .storage_data_relationships import Storage_data_relationships
    from .type_object import Type_object

@dataclass
class Storage_data(AdditionalDataHolder, Parsable):
    """
    An object containing information on the storage location.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ID to uniquely identify the storage location.
    id: Optional[str] = None
    # Contains links to resources that are directly related to the storage location.
    relationships: Optional[Storage_data_relationships] = None
    # The type of this resource. Possible values are ``objects``.
    type: Optional[Type_object] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Storage_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Storage_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Storage_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .storage_data_relationships import Storage_data_relationships
        from .type_object import Type_object

        from .storage_data_relationships import Storage_data_relationships
        from .type_object import Type_object

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(Storage_data_relationships)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_object)),
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
        writer.write_str_value("id", self.id)
        writer.write_object_value("relationships", self.relationships)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

