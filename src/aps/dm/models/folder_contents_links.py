from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_link import Json_api_link

@dataclass
class FolderContents_links(AdditionalDataHolder, Parsable):
    """
    Information on links for this resource. ``first``, ``prev``, and ``next`` are available only when the response is paginated.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object containing the hyperlink to the referenced resource.
    first: Optional[Json_api_link] = None
    # An object containing the hyperlink to the referenced resource.
    next: Optional[Json_api_link] = None
    # An object containing the hyperlink to the referenced resource.
    prev: Optional[Json_api_link] = None
    # An object containing the hyperlink to the referenced resource.
    self: Optional[Json_api_link] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FolderContents_links:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FolderContents_links
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FolderContents_links()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_link import Json_api_link

        from .json_api_link import Json_api_link

        fields: dict[str, Callable[[Any], None]] = {
            "first": lambda n : setattr(self, 'first', n.get_object_value(Json_api_link)),
            "next": lambda n : setattr(self, 'next', n.get_object_value(Json_api_link)),
            "prev": lambda n : setattr(self, 'prev', n.get_object_value(Json_api_link)),
            "self": lambda n : setattr(self, 'self', n.get_object_value(Json_api_link)),
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
        writer.write_object_value("first", self.first)
        writer.write_object_value("next", self.next)
        writer.write_object_value("prev", self.prev)
        writer.write_object_value("self", self.self)
        writer.write_additional_data_value(self.additional_data)
    

