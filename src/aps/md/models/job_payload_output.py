from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_payload_format import JobPayloadFormat
    from .job_payload_output_destination import JobPayload_output_destination

@dataclass
class JobPayload_output(AdditionalDataHolder, Parsable):
    """
    An object describing the attributes of the requested derivatives.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies where to store generated derivatives.
    destination: Optional[JobPayload_output_destination] = None
    # An array of objects, where each object represents a requested derivative format. You can request multiple derivatives.
    formats: Optional[list[JobPayloadFormat]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayload_output:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayload_output
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayload_output()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_payload_format import JobPayloadFormat
        from .job_payload_output_destination import JobPayload_output_destination

        from .job_payload_format import JobPayloadFormat
        from .job_payload_output_destination import JobPayload_output_destination

        fields: dict[str, Callable[[Any], None]] = {
            "destination": lambda n : setattr(self, 'destination', n.get_object_value(JobPayload_output_destination)),
            "formats": lambda n : setattr(self, 'formats', n.get_collection_of_object_values(JobPayloadFormat)),
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
        writer.write_object_value("destination", self.destination)
        writer.write_collection_of_object_values("formats", self.formats)
        writer.write_additional_data_value(self.additional_data)
    

