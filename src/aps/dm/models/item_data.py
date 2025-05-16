from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_attributes import ItemAttributes
    from .item_data_relationships import ItemData_relationships
    from .json_api_links_self_and_web_view import Json_api_links_self_and_web_view
    from .type_item import Type_item

@dataclass
class ItemData(AdditionalDataHolder, Parsable):
    """
    A container of data describing an item.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Properties of an item.
    attributes: Optional[ItemAttributes] = None
    # The unique identifier of the item.
    id: Optional[str] = None
    # Information on links to this resource.
    links: Optional[Json_api_links_self_and_web_view] = None
    # Contains links to resources that are directly related to this item.
    relationships: Optional[ItemData_relationships] = None
    # The type of the resource. Possible values are ``items``.
    type: Optional[Type_item] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_attributes import ItemAttributes
        from .item_data_relationships import ItemData_relationships
        from .json_api_links_self_and_web_view import Json_api_links_self_and_web_view
        from .type_item import Type_item

        from .item_attributes import ItemAttributes
        from .item_data_relationships import ItemData_relationships
        from .json_api_links_self_and_web_view import Json_api_links_self_and_web_view
        from .type_item import Type_item

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(ItemAttributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(Json_api_links_self_and_web_view)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(ItemData_relationships)),
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
    

