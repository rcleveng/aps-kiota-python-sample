from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .downloads_status import Downloads_status

@dataclass
class CreatedDownload_data_attributes(AdditionalDataHolder, Parsable):
    """
    Contains the properties that indicate the current status of the job.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The type of this resource. Possible values: queued, finished, failed, processing
    status: Optional[Downloads_status] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreatedDownload_data_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreatedDownload_data_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreatedDownload_data_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .downloads_status import Downloads_status

        from .downloads_status import Downloads_status

        fields: dict[str, Callable[[Any], None]] = {
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Downloads_status)),
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
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

