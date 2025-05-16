from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .version_payload_data_attributes_extension import VersionPayload_data_attributes_extension

@dataclass
class VersionPayload_data_attributes(AdditionalDataHolder, Parsable):
    """
    The properties of the version to be created.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Reserved for future use. Use ``data.attributes.name`` for the name.
    display_name: Optional[str] = None
    # A container of additional properties that extends the default properties of the version to be created.
    extension: Optional[VersionPayload_data_attributes_extension] = None
    # The file name to be used when synced to local disk (1-255 characters). Avoid using the following reserved characters in the name: ``<``, ``>``, ``:``, ``"``, ``/``, ``/``, ``|``, ``?``, ``*``, ``'``, ``/n``, ``/r``, ``/t``, ``/0``, ``/f``, ``¢``, ``™``, ``$``, ``®``.If you are creating the new version by copying an existing version of another item, the system uses the name of the source by default. However, if you specify a name, it will override the default name.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VersionPayload_data_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VersionPayload_data_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VersionPayload_data_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .version_payload_data_attributes_extension import VersionPayload_data_attributes_extension

        from .version_payload_data_attributes_extension import VersionPayload_data_attributes_extension

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(VersionPayload_data_attributes_extension)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("extension", self.extension)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

