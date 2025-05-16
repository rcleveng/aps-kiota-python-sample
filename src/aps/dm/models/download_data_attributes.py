from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .download_data_attributes_format import DownloadData_attributes_format

@dataclass
class DownloadData_attributes(AdditionalDataHolder, Parsable):
    """
    The properties of the download.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A container of the file format of the download.
    format: Optional[DownloadData_attributes_format] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadData_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadData_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadData_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .download_data_attributes_format import DownloadData_attributes_format

        from .download_data_attributes_format import DownloadData_attributes_format

        fields: dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(DownloadData_attributes_format)),
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
        writer.write_object_value("format", self.format)
        writer.write_additional_data_value(self.additional_data)
    

