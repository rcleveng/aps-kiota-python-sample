from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .download_formats_data_attributes import DownloadFormats_data_attributes
    from .type_downloadformats import Type_downloadformats

@dataclass
class DownloadFormats_data(AdditionalDataHolder, Parsable):
    """
    Contains information about the file formats the version can be downloaded as.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains the list of formats.
    attributes: Optional[DownloadFormats_data_attributes] = None
    # The URN of the version.
    id: Optional[str] = None
    # The type of this resource. Possible values are ``downloadFormats``.
    type: Optional[Type_downloadformats] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadFormats_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadFormats_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadFormats_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .download_formats_data_attributes import DownloadFormats_data_attributes
        from .type_downloadformats import Type_downloadformats

        from .download_formats_data_attributes import DownloadFormats_data_attributes
        from .type_downloadformats import Type_downloadformats

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_object_value(DownloadFormats_data_attributes)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_downloadformats)),
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
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

