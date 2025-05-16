from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .list_refs_attributes import ListRefs_attributes
    from .list_refs_included import ListRefs_included
    from .list_refs_relationships import ListRefs_relationships
    from .type_commands import Type_commands

@dataclass
class ListRefs(AdditionalDataHolder, Parsable):
    """
    The ``data`` object returned by the ListRefs command.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains the properties of the responseto the ListRefs command.
    attributes: Optional[ListRefs_attributes] = None
    # A unique ID assigned to the process executing the command.
    id: Optional[str] = None
    # An array of objects, where each object represents a referenced resource.
    included: Optional[list[ListRefs_included]] = None
    # Contains the list of versions that were checked. 
    relationships: Optional[ListRefs_relationships] = None
    # The type of this resource. Possible values are ``commands``.
    type: Optional[Type_commands] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListRefs:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListRefs
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListRefs()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .list_refs_attributes import ListRefs_attributes
        from .list_refs_included import ListRefs_included
        from .list_refs_relationships import ListRefs_relationships
        from .type_commands import Type_commands

        from .list_refs_attributes import ListRefs_attributes
        from .list_refs_included import ListRefs_included
        from .list_refs_relationships import ListRefs_relationships
        from .type_commands import Type_commands

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(ListRefs_attributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "included": lambda n : setattr(self, 'included', n.get_collection_of_object_values(ListRefs_included)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(ListRefs_relationships)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_commands)),
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
        writer.write_object_value("attributes", self.attributes)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("included", self.included)
        writer.write_object_value("relationships", self.relationships)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

