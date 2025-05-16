from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_links_self_and_web_view import Json_api_links_self_and_web_view
    from .type_version import Type_version
    from .version_attributes import VersionAttributes

@dataclass
class CreatedVersion_data(AdditionalDataHolder, Parsable):
    """
    A container of data describing the version.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The properties of a version.
    attributes: Optional[VersionAttributes] = None
    # The ID that uniquely identifies the version (Version ID). The Version ID is the URN of the version.
    id: Optional[str] = None
    # Information on links to this resource.
    links: Optional[Json_api_links_self_and_web_view] = None
    # The type of the resource. Possible values are ``versions``.
    type: Optional[Type_version] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreatedVersion_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreatedVersion_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreatedVersion_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_links_self_and_web_view import Json_api_links_self_and_web_view
        from .type_version import Type_version
        from .version_attributes import VersionAttributes

        from .json_api_links_self_and_web_view import Json_api_links_self_and_web_view
        from .type_version import Type_version
        from .version_attributes import VersionAttributes

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(VersionAttributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(Json_api_links_self_and_web_view)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_version)),
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
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

