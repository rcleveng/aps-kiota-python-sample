from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hub_data_attributes import HubData_attributes
    from .hub_data_relationships import HubData_relationships
    from .json_api_links_self import Json_api_links_self
    from .type_hub import Type_hub

@dataclass
class HubData(AdditionalDataHolder, Parsable):
    """
    The object containing information about the hub.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The properties of the hub.
    attributes: Optional[HubData_attributes] = None
    # The hub ID, which uniquely identifies the hub.
    id: Optional[str] = None
    # An object containing the URI of the endpoint to access this resource.
    links: Optional[Json_api_links_self] = None
    # Contains links to resources that are directly related to this hub.
    relationships: Optional[HubData_relationships] = None
    # The type of the resource. Possible values are ``hubs``.
    type: Optional[Type_hub] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HubData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HubData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HubData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .hub_data_attributes import HubData_attributes
        from .hub_data_relationships import HubData_relationships
        from .json_api_links_self import Json_api_links_self
        from .type_hub import Type_hub

        from .hub_data_attributes import HubData_attributes
        from .hub_data_relationships import HubData_relationships
        from .json_api_links_self import Json_api_links_self
        from .type_hub import Type_hub

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(HubData_attributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(Json_api_links_self)),
            "relationships": lambda n : setattr(self, 'relationships', n.get_object_value(HubData_relationships)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_hub)),
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
    

