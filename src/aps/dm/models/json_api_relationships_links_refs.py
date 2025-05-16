from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_relationships_links_refs_links import Json_api_relationships_links_refs_links

@dataclass
class Json_api_relationships_links_refs(AdditionalDataHolder, Parsable):
    """
    Information on other resources that have a custom relationship with this resource.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The object containing information on links of related resources that share a custom relationship with this resource.
    links: Optional[Json_api_relationships_links_refs_links] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Json_api_relationships_links_refs:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Json_api_relationships_links_refs
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Json_api_relationships_links_refs()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_relationships_links_refs_links import Json_api_relationships_links_refs_links

        from .json_api_relationships_links_refs_links import Json_api_relationships_links_refs_links

        fields: dict[str, Callable[[Any], None]] = {
            "links": lambda n : setattr(self, 'links', n.get_object_value(Json_api_relationships_links_refs_links)),
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
        writer.write_object_value("links", self.links)
        writer.write_additional_data_value(self.additional_data)
    

