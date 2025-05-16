from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_links_related import Json_api_links_related
    from .json_api_links_self import Json_api_links_self

@dataclass
class RelationshipRefs_links(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes Json_api_links_related, Json_api_links_self
    """
    # Composed type representation for type Json_api_links_related
    json_api_links_related: Optional[Json_api_links_related] = None
    # Composed type representation for type Json_api_links_self
    json_api_links_self: Optional[Json_api_links_self] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelationshipRefs_links:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelationshipRefs_links
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = RelationshipRefs_links()
        if mapping_value and mapping_value.casefold() == "json_api_links_related".casefold():
            from .json_api_links_related import Json_api_links_related

            result.json_api_links_related = Json_api_links_related()
        elif mapping_value and mapping_value.casefold() == "json_api_links_self".casefold():
            from .json_api_links_self import Json_api_links_self

            result.json_api_links_self = Json_api_links_self()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_links_related import Json_api_links_related
        from .json_api_links_self import Json_api_links_self

        if self.json_api_links_related:
            return self.json_api_links_related.get_field_deserializers()
        if self.json_api_links_self:
            return self.json_api_links_self.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.json_api_links_related:
            writer.write_object_value(None, self.json_api_links_related)
        elif self.json_api_links_self:
            writer.write_object_value(None, self.json_api_links_self)
    

