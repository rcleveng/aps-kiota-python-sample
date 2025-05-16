from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .buckets_items import Buckets_items

@dataclass
class Buckets(AdditionalDataHolder, Parsable):
    """
    An object that represents a collection of buckets.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Array of objects, where each object represents a bucket.
    items: Optional[list[Buckets_items]] = None
    # The URL to be used to retrieve the next page of results, if available. It will be present only when there are more items to be retrieved after the current set.
    next: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Buckets:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Buckets
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Buckets()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .buckets_items import Buckets_items

        from .buckets_items import Buckets_items

        fields: dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(Buckets_items)),
            "next": lambda n : setattr(self, 'next', n.get_str_value()),
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
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("next", self.next)
        writer.write_additional_data_value(self.additional_data)
    

