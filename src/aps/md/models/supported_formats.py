from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .supported_formats_formats import SupportedFormats_formats

@dataclass
class SupportedFormats(AdditionalDataHolder, Parsable):
    """
    An object that represents the successful response of a List Supported Formats operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A dictionary object that contains a collection of key-value pairs, where each pair represents the target file format and the corresponding source file formats.
    formats: Optional[SupportedFormats_formats] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SupportedFormats:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SupportedFormats
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SupportedFormats()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .supported_formats_formats import SupportedFormats_formats

        from .supported_formats_formats import SupportedFormats_formats

        fields: dict[str, Callable[[Any], None]] = {
            "formats": lambda n : setattr(self, 'formats', n.get_object_value(SupportedFormats_formats)),
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
        writer.write_object_value("formats", self.formats)
        writer.write_additional_data_value(self.additional_data)
    

