from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_link import Json_api_link
    from .version_extension_with_schema_link_data import Version_extension_with_schema_link_data

@dataclass
class Version_extension_with_schema_link(AdditionalDataHolder, Parsable):
    """
    A container of additional properties that extends the default properties of a version.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The object that contains the additional properties, which makes this resource extensible.
    data: Optional[Version_extension_with_schema_link_data] = None
    # An object containing the hyperlink to the referenced resource.
    schema: Optional[Json_api_link] = None
    # The Type ID of the schema that defines the structure of the ``extension.data`` object.
    type: Optional[str] = None
    # The version of the schema that applies to the ``extension.data`` object.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Version_extension_with_schema_link:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Version_extension_with_schema_link
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Version_extension_with_schema_link()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_link import Json_api_link
        from .version_extension_with_schema_link_data import Version_extension_with_schema_link_data

        from .json_api_link import Json_api_link
        from .version_extension_with_schema_link_data import Version_extension_with_schema_link_data

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(Version_extension_with_schema_link_data)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(Json_api_link)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("schema", self.schema)
        writer.write_str_value("type", self.type)
        writer.write_str_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

