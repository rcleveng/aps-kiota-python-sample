from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .created_version_included_links import CreatedVersion_included_links
    from .created_version_included_relationships import CreatedVersion_included_relationships
    from .item_attributes import ItemAttributes
    from .type_item import Type_item

@dataclass
class CreatedVersion_included(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Properties of an item.
    attributes: Optional[ItemAttributes] = None
    # The ID to uniquely identify the resource.
    id: Optional[str] = None
    # Contains the links to use to access references of this resource.
    links: Optional[CreatedVersion_included_links] = None
    # Contains links to resources that are directly related to this item.
    relationships: Optional[CreatedVersion_included_relationships] = None
    # The type of the resource. Possible values are ``items``.
    type: Optional[Type_item] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreatedVersion_included:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreatedVersion_included
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreatedVersion_included()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .created_version_included_links import CreatedVersion_included_links
        from .created_version_included_relationships import CreatedVersion_included_relationships
        from .item_attributes import ItemAttributes
        from .type_item import Type_item

        from .created_version_included_links import CreatedVersion_included_links
        from .created_version_included_relationships import CreatedVersion_included_relationships
        from .item_attributes import ItemAttributes
        from .type_item import Type_item

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(ItemAttributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(CreatedVersion_included_links)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(CreatedVersion_included_relationships)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_item)),
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
        writer.write_object_value("links", self.links)
        writer.write_object_value("relationships", self.relationships)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

