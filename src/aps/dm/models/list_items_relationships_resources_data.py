from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_data import ItemData
    from .type_item import Type_item

@dataclass
class ListItems_relationships_resources_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The URN of the item.
    id: Optional[str] = None
    # A container of data describing an item.
    meta: Optional[ItemData] = None
    # The type of the resource. Possible values are ``items``.
    type: Optional[Type_item] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListItems_relationships_resources_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListItems_relationships_resources_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListItems_relationships_resources_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_data import ItemData
        from .type_item import Type_item

        from .item_data import ItemData
        from .type_item import Type_item

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(ItemData)),
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
        writer.write_str_value("id", self.id)
        writer.write_object_value("meta", self.meta)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

