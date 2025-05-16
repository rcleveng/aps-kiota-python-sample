from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_payload_data import ItemPayload_data
    from .item_payload_included import ItemPayload_included
    from .json_api_version import Json_api_version
    from .meta_for_webhooks import MetaForWebhooks

@dataclass
class ItemPayload(AdditionalDataHolder, Parsable):
    """
    Describe the item to be created.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The data that describes the item to be created.
    data: Optional[ItemPayload_data] = None
    # An array of objects, where each object represents a version of the item to be created. In this case there will only be one element in the array.
    included: Optional[list[ItemPayload_included]] = None
    # The JSON API object.
    jsonapi: Optional[Json_api_version] = None
    # Meta information required for webhooks.
    meta: Optional[MetaForWebhooks] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_payload_data import ItemPayload_data
        from .item_payload_included import ItemPayload_included
        from .json_api_version import Json_api_version
        from .meta_for_webhooks import MetaForWebhooks

        from .item_payload_data import ItemPayload_data
        from .item_payload_included import ItemPayload_included
        from .json_api_version import Json_api_version
        from .meta_for_webhooks import MetaForWebhooks

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(ItemPayload_data)),
            "included": lambda n : setattr(self, 'included', n.get_collection_of_object_values(ItemPayload_included)),
            "jsonapi": lambda n : setattr(self, 'jsonapi', n.get_object_value(Json_api_version)),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(MetaForWebhooks)),
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
        writer.write_object_value("data", self.data)
        writer.write_collection_of_object_values("included", self.included)
        writer.write_object_value("jsonapi", self.jsonapi)
        writer.write_object_value("meta", self.meta)
        writer.write_additional_data_value(self.additional_data)
    

