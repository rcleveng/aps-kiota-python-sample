from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_data import ItemData
    from .version_data import VersionData

@dataclass
class ListRefs_included(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes ItemData, VersionData
    """
    # Composed type representation for type ItemData
    item_data: Optional[ItemData] = None
    # Composed type representation for type VersionData
    version_data: Optional[VersionData] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListRefs_included:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListRefs_included
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = ListRefs_included()
        if mapping_value and mapping_value.casefold() == "ItemData".casefold():
            from .item_data import ItemData

            result.item_data = ItemData()
        elif mapping_value and mapping_value.casefold() == "VersionData".casefold():
            from .version_data import VersionData

            result.version_data = VersionData()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_data import ItemData
        from .version_data import VersionData

        if self.item_data:
            return self.item_data.get_field_deserializers()
        if self.version_data:
            return self.version_data.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.item_data:
            writer.write_object_value(None, self.item_data)
        elif self.version_data:
            writer.write_object_value(None, self.version_data)
    

