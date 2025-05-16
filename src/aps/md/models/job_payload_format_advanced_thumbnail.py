from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JobPayloadFormatAdvancedThumbnail(AdditionalDataHolder, Parsable):
    """
    An object that contains advanced options for a thumbnail output.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Height of thumbnails. Possible values are: ``100``, ``200``, ``400``.If ``height`` is omitted, but ``width`` is specified, ``height`` defaults to ``width``.  If both ``width`` and ``height`` are omitted, the server will return a thumbnail closest to ``200``, if such a thumbnail is available
    height: Optional[int] = None
    # Width of thumbnail in pixels.  Possible values are: ``100``, ``200``, ``400``  If ``width`` is omitted, but ``height`` is specified, ``width`` defaults to ``height``. If both ``width`` and ``height`` are omitted, the server will return a thumbnail closest to ``200``, if such a thumbnail is available.
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormatAdvancedThumbnail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormatAdvancedThumbnail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayloadFormatAdvancedThumbnail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_int_value("height", self.height)
        writer.write_int_value("width", self.width)
        writer.write_additional_data_value(self.additional_data)
    

