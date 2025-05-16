from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .download_payload_data_relationships_source_data import DownloadPayload_data_relationships_source_data

@dataclass
class DownloadPayload_data_relationships_source(AdditionalDataHolder, Parsable):
    """
    Contains information about the version the download format is being created for.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains information about the version the download format is being created for.
    data: Optional[DownloadPayload_data_relationships_source_data] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadPayload_data_relationships_source:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadPayload_data_relationships_source
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadPayload_data_relationships_source()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .download_payload_data_relationships_source_data import DownloadPayload_data_relationships_source_data

        from .download_payload_data_relationships_source_data import DownloadPayload_data_relationships_source_data

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(DownloadPayload_data_relationships_source_data)),
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
        writer.write_additional_data_value(self.additional_data)
    

