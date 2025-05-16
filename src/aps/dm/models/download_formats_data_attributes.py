from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .download_formats_data_attributes_formats import DownloadFormats_data_attributes_formats

@dataclass
class DownloadFormats_data_attributes(AdditionalDataHolder, Parsable):
    """
    Contains the list of formats.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of objects, where each object corresponds to a file format.
    formats: Optional[list[DownloadFormats_data_attributes_formats]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadFormats_data_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadFormats_data_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadFormats_data_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .download_formats_data_attributes_formats import DownloadFormats_data_attributes_formats

        from .download_formats_data_attributes_formats import DownloadFormats_data_attributes_formats

        fields: dict[str, Callable[[Any], None]] = {
            "formats": lambda n : setattr(self, 'formats', n.get_collection_of_object_values(DownloadFormats_data_attributes_formats)),
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
        writer.write_collection_of_object_values("formats", self.formats)
        writer.write_additional_data_value(self.additional_data)
    

