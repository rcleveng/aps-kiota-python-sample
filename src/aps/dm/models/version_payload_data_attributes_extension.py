from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .version_payload_data_attributes_extension_data import VersionPayload_data_attributes_extension_data

@dataclass
class VersionPayload_data_attributes_extension(AdditionalDataHolder, Parsable):
    """
    A container of additional properties that extends the default properties of the version to be created.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The container of additional properties.The additional properties must follow the schema specified by ``extensions.type`` and ``extensions.version``. Properties that don't follow the schema will be ignored.
    data: Optional[VersionPayload_data_attributes_extension_data] = None
    # The Type ID of the schema that defines the structure of the ``extension.data`` object.
    type: Optional[str] = None
    # The version of the schema that applies to the ``extension.data`` object.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VersionPayload_data_attributes_extension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VersionPayload_data_attributes_extension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VersionPayload_data_attributes_extension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .version_payload_data_attributes_extension_data import VersionPayload_data_attributes_extension_data

        from .version_payload_data_attributes_extension_data import VersionPayload_data_attributes_extension_data

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(VersionPayload_data_attributes_extension_data)),
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
        writer.write_str_value("type", self.type)
        writer.write_str_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

