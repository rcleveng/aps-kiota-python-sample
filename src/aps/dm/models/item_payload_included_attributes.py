from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_payload_included_attributes_extension import ItemPayload_included_attributes_extension

@dataclass
class ItemPayload_included_attributes(AdditionalDataHolder, Parsable):
    """
    The properties of the first version of the item to be created.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A container of additional properties that extends the default properties of this resource.
    extension: Optional[ItemPayload_included_attributes_extension] = None
    # The name of the version (1-255 characters).Avoid using the following reserved characters in the name: ``<``, ``>``, ``:``, ``"``, ``/``, ``/``, ``|``, ``?``, ``*``, ``'``, ``/n``, ``/r``, ``/t``, ``/0``, ``/f``, ``¢``, ``™``, ``$If you are creating a new item by copying a version of an existing item, the name defaults to the name of the source version.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemPayload_included_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemPayload_included_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemPayload_included_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_payload_included_attributes_extension import ItemPayload_included_attributes_extension

        from .item_payload_included_attributes_extension import ItemPayload_included_attributes_extension

        fields: dict[str, Callable[[Any], None]] = {
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(ItemPayload_included_attributes_extension)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_object_value("extension", self.extension)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

