from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_payload_input import JobPayload_input
    from .job_payload_misc import JobPayload_misc
    from .job_payload_output import JobPayload_output

@dataclass
class JobPayload(AdditionalDataHolder, Parsable):
    """
    An object that represents the request body of a Create Translation Job operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object describing the attributes of the source design.
    input: Optional[JobPayload_input] = None
    # A collection of miscellaneous parameters.
    misc: Optional[JobPayload_misc] = None
    # An object describing the attributes of the requested derivatives.
    output: Optional[JobPayload_output] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_payload_input import JobPayload_input
        from .job_payload_misc import JobPayload_misc
        from .job_payload_output import JobPayload_output

        from .job_payload_input import JobPayload_input
        from .job_payload_misc import JobPayload_misc
        from .job_payload_output import JobPayload_output

        fields: dict[str, Callable[[Any], None]] = {
            "input": lambda n : setattr(self, 'input', n.get_object_value(JobPayload_input)),
            "misc": lambda n : setattr(self, 'misc', n.get_object_value(JobPayload_misc)),
            "output": lambda n : setattr(self, 'output', n.get_object_value(JobPayload_output)),
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
        writer.write_object_value("input", self.input)
        writer.write_object_value("misc", self.misc)
        writer.write_object_value("output", self.output)
        writer.write_additional_data_value(self.additional_data)
    

