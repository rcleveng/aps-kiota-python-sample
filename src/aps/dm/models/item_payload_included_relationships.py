from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_payload_included_relationships_storage import ItemPayload_included_relationships_storage
    from .json_api_relationships_refs import Json_api_relationships_refs

@dataclass
class ItemPayload_included_relationships(AdditionalDataHolder, Parsable):
    """
    A container of links to resources that are related to the item to be created.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Information on other resources that share a custom relationship with this resource.
    refs: Optional[Json_api_relationships_refs] = None
    # The object containing information on where the binary data of the item is stored.
    storage: Optional[ItemPayload_included_relationships_storage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemPayload_included_relationships:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemPayload_included_relationships
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemPayload_included_relationships()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_payload_included_relationships_storage import ItemPayload_included_relationships_storage
        from .json_api_relationships_refs import Json_api_relationships_refs

        from .item_payload_included_relationships_storage import ItemPayload_included_relationships_storage
        from .json_api_relationships_refs import Json_api_relationships_refs

        fields: dict[str, Callable[[Any], None]] = {
            "refs": lambda n : setattr(self, 'refs', n.get_object_value(Json_api_relationships_refs)),
            "storage": lambda n : setattr(self, 'storage', n.get_object_value(ItemPayload_included_relationships_storage)),
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
        writer.write_object_value("refs", self.refs)
        writer.write_object_value("storage", self.storage)
        writer.write_additional_data_value(self.additional_data)
    

